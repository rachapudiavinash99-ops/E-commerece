"""
Module: Functional Programming Paradigms in Python 3.12
Covers Pure Functions, Higher-Order Functions, Functors, Monads (Maybe, Either, IO),
Currying, Partial Application, Function Composition, and Trampolining for Recursion.
"""

import functools
from typing import Callable, TypeVar, Generic, Any, List, Optional, Union

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
E = TypeVar('E')


# ============================================================================
# 1. FUNCTION COMPOSITION & PIPING
# ============================================================================

class Pipe:
    """Fluid function piping wrapper supporting binary pipe '|' operator."""

    def __init__(self, value: Any) -> None:
        self.value = value

    def __or__(self, func: Callable[[Any], Any]) -> 'Pipe':
        return Pipe(func(self.value))

    def unwrap(self) -> Any:
        return self.value


def compose(*functions: Callable) -> Callable:
    """Right-to-left function composition: compose(f, g, h)(x) == f(g(h(x)))."""
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def pipe(*functions: Callable) -> Callable:
    """Left-to-right function piping: pipe(f, g, h)(x) == h(g(f(x)))."""
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)


def curry(func: Callable) -> Callable:
    """Currying decorator transforming multi-argument function into unary sequence."""
    @functools.wraps(func)
    def curried(*args: Any, **kwargs: Any) -> Any:
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    return curried


# ============================================================================
# 2. MONADIC ABSTRACTIONS (Maybe, Either, Result)
# ============================================================================

class Maybe(Generic[A]):
    """Maybe Monad encapsulating optional values without NullPointer/NoneType errors."""

    def __init__(self, value: Optional[A]) -> None:
        self._value: Optional[A] = value

    @classmethod
    def some(cls, val: A) -> 'Maybe[A]':
        return cls(val)

    @classmethod
    def nothing(cls) -> 'Maybe[A]':
        return cls(None)

    def is_some(self) -> bool:
        return self._value is not None

    def is_nothing(self) -> bool:
        return self._value is None

    def map(self, fn: Callable[[A], B]) -> 'Maybe[B]':
        if self.is_nothing():
            return Maybe.nothing()
        return Maybe.some(fn(self._value))  # type: ignore

    def bind(self, fn: Callable[[A], 'Maybe[B]']) -> 'Maybe[B]':
        if self.is_nothing():
            return Maybe.nothing()
        return fn(self._value)  # type: ignore

    def get_or_else(self, default: A) -> A:
        return self._value if self.is_some() else default


class Either(Generic[E, A]):
    """Either Monad (Left for failure, Right for success value)."""

    def __init__(self, is_right: bool, left_val: Optional[E] = None, right_val: Optional[A] = None) -> None:
        self._is_right = is_right
        self._left = left_val
        self._right = right_val

    @classmethod
    def right(cls, value: A) -> 'Either[E, A]':
        return cls(True, right_val=value)

    @classmethod
    def left(cls, error: E) -> 'Either[E, A]':
        return cls(False, left_val=error)

    def map(self, fn: Callable[[A], B]) -> 'Either[E, B]':
        if not self._is_right:
            return Either.left(self._left)  # type: ignore
        return Either.right(fn(self._right))  # type: ignore

    def bind(self, fn: Callable[[A], 'Either[E, B]']) -> 'Either[E, B]':
        if not self._is_right:
            return Either.left(self._left)  # type: ignore
        return fn(self._right)  # type: ignore

    def is_success(self) -> bool:
        return self._is_right


# ============================================================================
# 3. TRAMPOLINE FOR TAIL-CALL OPTIMIZATION
# ============================================================================

class Trampoline:
    """Trampolining helper preventing Python RecursionError for deep recursive pipelines."""

    @staticmethod
    def run(thunk: Any) -> Any:
        while callable(thunk):
            thunk = thunk()
        return thunk
