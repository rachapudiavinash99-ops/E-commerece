"""
Module: Distributed Transactions, SAGA Pattern Orchestration, and Outbox Pattern
"""

import time
import uuid
from typing import Dict, List, Any, Callable, Optional


class SagaStep:
    """A single executable step in a SAGA with forward action and compensating rollback."""

    def __init__(
        self,
        name: str,
        action: Callable[[Dict[str, Any]], Any],
        compensation: Callable[[Dict[str, Any]], Any]
    ) -> None:
        self.name = name
        self.action = action
        self.compensation = compensation


class SagaOrchestrator:
    """
    Saga Pattern Orchestrator coordinating multi-service distributed transactions
    with automated compensating transactions upon step failure.
    """

    def __init__(self, saga_name: str) -> None:
        self.saga_name = saga_name
        self.steps: List[SagaStep] = []
        self.execution_log: List[Dict[str, Any]] = []

    def add_step(self, step: SagaStep) -> 'SagaOrchestrator':
        self.steps.append(step)
        return self

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        executed_steps: List[SagaStep] = []
        context = dict(payload)

        for step in self.steps:
            try:
                print(f"[SAGA {self.saga_name}] Executing step: {step.name}")
                result = step.action(context)
                context[f"{step.name}_result"] = result
                executed_steps.append(step)
                self.execution_log.append({"step": step.name, "status": "COMPLETED"})
            except Exception as exc:
                print(f"[SAGA {self.saga_name}] Step {step.name} FAILED: {exc}. Triggering compensations...")
                self.execution_log.append({"step": step.name, "status": "FAILED", "error": str(exc)})
                self._compensate(executed_steps, context)
                return {
                    "saga": self.saga_name,
                    "status": "COMPENSATED",
                    "failed_step": step.name,
                    "error": str(exc),
                    "log": self.execution_log
                }

        return {
            "saga": self.saga_name,
            "status": "SUCCESS",
            "log": self.execution_log,
            "context": context
        }

    def _compensate(self, executed_steps: List[SagaStep], context: Dict[str, Any]) -> None:
        for step in reversed(executed_steps):
            try:
                print(f"[SAGA {self.saga_name}] Rolling back compensation: {step.name}")
                step.compensation(context)
                self.execution_log.append({"step": step.name, "status": "COMPENSATED"})
            except Exception as comp_err:
                print(f"[SAGA CRITICAL] Compensation failed for {step.name}: {comp_err}")
                self.execution_log.append({"step": step.name, "status": "COMPENSATION_ERROR", "error": str(comp_err)})
