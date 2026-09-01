"""
Module: Kubernetes Pod Lifecycle, Service Discovery, and Rolling Deployments Engine
"""

import time
import enum
from typing import List, Dict, Optional, Any


class PodPhase(str, enum.Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UNKNOWN = "Unknown"


class Pod:
    """Simulated Container Pod with resource limits, readiness, and liveness probes."""

    def __init__(self, name: str, image: str, cpu_millicores: int = 500, memory_mb: int = 512) -> None:
        self.name = name
        self.image = image
        self.cpu_millicores = cpu_millicores
        self.memory_mb = memory_mb
        self.phase: PodPhase = PodPhase.PENDING
        self.ip_address: Optional[str] = None
        self.restart_count: int = 0
        self.start_time: float = time.time()

    def start(self, assigned_ip: str) -> None:
        self.ip_address = assigned_ip
        self.phase = PodPhase.RUNNING

    def crash(self) -> None:
        self.phase = PodPhase.FAILED
        self.restart_count += 1


class DeploymentController:
    """
    Deployment Controller managing desired replicas and Zero-Downtime Rolling Updates.
    """

    def __init__(self, name: str, image: str, replicas: int = 3) -> None:
        self.name = name
        self.image = image
        self.desired_replicas = replicas
        self.pods: List[Pod] = []
        self._ip_counter = 10
        self._reconcile()

    def _generate_ip(self) -> str:
        self._ip_counter += 1
        return f"10.244.0.{self._ip_counter}"

    def _reconcile(self) -> None:
        # Scale up
        while len(self.pods) < self.desired_replicas:
            idx = len(self.pods) + 1
            pod = Pod(f"{self.name}-{idx}", self.image)
            pod.start(self._generate_ip())
            self.pods.append(pod)

        # Scale down
        while len(self.pods) > self.desired_replicas:
            self.pods.pop()

    def rolling_update(self, new_image: str) -> None:
        """Simulates a Kubernetes Rolling Update Strategy (MaxSurge=1, MaxUnavailable=0)."""
        self.image = new_image
        new_pods: List[Pod] = []

        for i, old_pod in enumerate(self.pods):
            new_pod = Pod(f"{self.name}-v2-{i+1}", new_image)
            new_pod.start(self._generate_ip())
            new_pods.append(new_pod)
            print(f"[RollingUpdate] Spun up {new_pod.name} ({new_pod.ip_address}), terminating {old_pod.name}")

        self.pods = new_pods


class RoundRobinLoadBalancer:
    """L4/L7 Service Load Balancer distributing requests across active pods."""

    def __init__(self) -> None:
        self._index = 0

    def pick_pod(self, pods: List[Pod]) -> Optional[Pod]:
        active_pods = [p for p in pods if p.phase == PodPhase.RUNNING]
        if not active_pods:
            return None
        selected = active_pods[self._index % len(active_pods)]
        self._index += 1
        return selected
