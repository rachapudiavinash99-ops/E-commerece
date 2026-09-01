"""
Module: Advanced Python Concurrency, Asyncio Event Loops, and Actor Model
"""

import asyncio
import threading
import queue
import time
from typing import Callable, Any, List, Dict, Optional, Coroutine


class ThreadPoolWorker:
    """Custom Thread Pool implementation demonstrating thread synchronization and work queues."""

    def __init__(self, num_threads: int = 4) -> None:
        self.num_threads = num_threads
        self.tasks: queue.Queue = queue.Queue()
        self.threads: List[threading.Thread] = []
        self._shutdown = False
        self._lock = threading.Lock()
        self._init_workers()

    def _worker_loop(self) -> None:
        while not self._shutdown:
            try:
                func, args, kwargs, future_result = self.tasks.get(timeout=0.1)
                try:
                    result = func(*args, **kwargs)
                    future_result.set_result(result)
                except Exception as ex:
                    future_result.set_exception(ex)
                finally:
                    self.tasks.task_done()
            except queue.Empty:
                continue

    def _init_workers(self) -> None:
        for i in range(self.num_threads):
            t = threading.Thread(target=self._worker_loop, name=f"WorkerThread-{i}", daemon=True)
            t.start()
            self.threads.append(t)

    def submit(self, func: Callable, *args: Any, **kwargs: Any) -> 'FutureResult':
        with self._lock:
            if self._shutdown:
                raise RuntimeError("Cannot submit to shutdown pool")
            future = FutureResult()
            self.tasks.put((func, args, kwargs, future))
            return future

    def shutdown(self, wait: bool = True) -> None:
        self._shutdown = True
        if wait:
            for t in self.threads:
                t.join()


class FutureResult:
    """Thread-safe Future container for asynchronous worker results."""

    def __init__(self) -> None:
        self._result: Any = None
        self._exception: Optional[Exception] = None
        self._event = threading.Event()

    def set_result(self, result: Any) -> None:
        self._result = result
        self._event.set()

    def set_exception(self, exc: Exception) -> None:
        self._exception = exc
        self._event.set()

    def get(self, timeout: Optional[float] = None) -> Any:
        if not self._event.wait(timeout):
            raise TimeoutError("Task result timed out")
        if self._exception:
            raise self._exception
        return self._result


class AsyncRateLimiter:
    """Asynchronous Token Bucket rate limiter for Asyncio coroutines."""

    def __init__(self, rate: float, capacity: float) -> None:
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self, tokens: float = 1.0) -> None:
        async with self._lock:
            while True:
                now = time.monotonic()
                elapsed = now - self.last_update
                self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
                self.last_update = now

                if self.tokens >= tokens:
                    self.tokens -= tokens
                    return
                # Calculate sleep duration until tokens available
                missing = tokens - self.tokens
                sleep_sec = missing / self.rate
                await asyncio.sleep(sleep_sec)


class Actor:
    """Actor Model message-passing concurrency pattern in Asyncio."""

    def __init__(self) -> None:
        self._mailbox: asyncio.Queue = asyncio.Queue()
        self._task: Optional[asyncio.Task] = None

    async def start(self) -> None:
        self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        if self._task:
            self._task.cancel()

    async def send(self, message: Any) -> None:
        await self._mailbox.put(message)

    async def _run(self) -> None:
        while True:
            msg = await self._mailbox.get()
            try:
                await self.handle_message(msg)
            finally:
                self._mailbox.task_done()

    async def handle_message(self, message: Any) -> None:
        raise NotImplementedError("Subclasses must implement handle_message")
