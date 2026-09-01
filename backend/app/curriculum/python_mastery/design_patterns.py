"""
Module: Gang of Four (GoF) and Enterprise Design Patterns in Python 3.12
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Callable


# ============================================================================
# CREATIONAL PATTERNS
# ============================================================================

class SingletonMeta(type):
    """Thread-safe Singleton Metaclass implementation."""
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnectionPool(metaclass=SingletonMeta):
    def __init__(self, pool_size: int = 10) -> None:
        self.pool_size = pool_size
        self.active_connections = 0

    def get_connection(self) -> str:
        self.active_connections += 1
        return f"Conn-{self.active_connections}"


class CourseFactory:
    """Factory Method pattern for dynamic course curriculum creation."""

    @staticmethod
    def create_course_module(module_type: str, title: str) -> Dict[str, Any]:
        types = {
            "foundations": {"title": title, "difficulty": "beginner", "estimated_hours": 10},
            "architecture": {"title": title, "difficulty": "advanced", "estimated_hours": 25},
            "microservices": {"title": title, "difficulty": "intermediate", "estimated_hours": 18}
        }
        if module_type not in types:
            raise ValueError(f"Unknown module type: {module_type}")
        return types[module_type]


# ============================================================================
# STRUCTURAL PATTERNS
# ============================================================================

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        pass


class StripeAPIService:
    def make_charge(self, cents: int, curr: str) -> str:
        return f"ch_stripe_{cents}_{curr}"


class StripeAdapter(PaymentProcessor):
    """Adapter Pattern adapting Stripe SDK interface to standardized PaymentProcessor."""

    def __init__(self, stripe_service: StripeAPIService) -> None:
        self.service = stripe_service

    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        cents = int(amount * 100)
        charge_id = self.service.make_charge(cents, currency.lower())
        return {"status": "success", "charge_id": charge_id, "amount": amount}


# ============================================================================
# BEHAVIORAL PATTERNS
# ============================================================================

class Observer(ABC):
    @abstractmethod
    def notify(self, event_name: str, payload: Any) -> None:
        pass


class EventDispatcher:
    """Observer / Pub-Sub pattern for decoupling cross-domain events."""

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Observer]] = {}

    def subscribe(self, event_name: str, observer: Observer) -> None:
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(observer)

    def publish(self, event_name: str, payload: Any) -> None:
        if event_name in self._subscribers:
            for obs in self._subscribers[event_name]:
                obs.notify(event_name, payload)


class EmailNotifier(Observer):
    def notify(self, event_name: str, payload: Any) -> None:
        print(f"[Email Notification] Event: {event_name}, Data: {payload}")


class CertificateIssuer(Observer):
    def notify(self, event_name: str, payload: Any) -> None:
        if event_name == "course.completed":
            print(f"[Certificate Triggered] Generating cert for {payload}")


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, original_price: float) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply_discount(self, original_price: float) -> float:
        return round(original_price * (1 - self.percent / 100.0), 2)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def apply_discount(self, original_price: float) -> float:
        return max(0.0, round(original_price - self.amount, 2))
