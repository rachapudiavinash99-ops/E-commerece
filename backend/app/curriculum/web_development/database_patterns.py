"""
Module: Enterprise Database Patterns (Unit of Work, CQRS, Event Sourcing & Connection Pooling)
"""

import time
import uuid
from typing import Dict, List, Any, Optional, Callable
from abc import ABC, abstractmethod


class DomainEvent:
    """Base Domain Event in Event Sourcing architecture."""

    def __init__(self, aggregate_id: str, event_type: str, data: Dict[str, Any]) -> None:
        self.event_id = str(uuid.uuid4())
        self.aggregate_id = aggregate_id
        self.event_type = event_type
        self.data = data
        self.timestamp = time.time()


class EventStore:
    """Immutable Append-Only Event Store for Auditing and Event Sourcing."""

    def __init__(self) -> None:
        self.events: List[DomainEvent] = []
        self._subscribers: List[Callable[[DomainEvent], None]] = []

    def append(self, event: DomainEvent) -> None:
        self.events.append(event)
        for sub in self._subscribers:
            sub(event)

    def subscribe(self, callback: Callable[[DomainEvent], None]) -> None:
        self._subscribers.append(callback)

    def get_events_for_aggregate(self, aggregate_id: str) -> List[DomainEvent]:
        return [e for e in self.events if e.aggregate_id == aggregate_id]


class UnitOfWork(ABC):
    """
    Unit of Work pattern maintaining a list of business objects affected by a business transaction
    and coordinating the writing out of changes and the resolution of concurrency problems.
    """

    def __init__(self) -> None:
        self.new_objects: List[Any] = []
        self.dirty_objects: List[Any] = []
        self.removed_objects: List[Any] = []

    def register_new(self, entity: Any) -> None:
        if entity not in self.new_objects:
            self.new_objects.append(entity)

    def register_dirty(self, entity: Any) -> None:
        if entity not in self.dirty_objects and entity not in self.new_objects:
            self.dirty_objects.append(entity)

    def register_removed(self, entity: Any) -> None:
        if entity in self.new_objects:
            self.new_objects.remove(entity)
            return
        if entity in self.dirty_objects:
            self.dirty_objects.remove(entity)
        if entity not in self.removed_objects:
            self.removed_objects.append(entity)

    @abstractmethod
    def commit(self) -> bool:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass


class InMemoryUnitOfWork(UnitOfWork):
    def commit(self) -> bool:
        print(f"[UnitOfWork Commit] Inserting {len(self.new_objects)} new, updating {len(self.dirty_objects)}, removing {len(self.removed_objects)}")
        self.new_objects.clear()
        self.dirty_objects.clear()
        self.removed_objects.clear()
        return True

    def rollback(self) -> None:
        self.new_objects.clear()
        self.dirty_objects.clear()
        self.removed_objects.clear()
