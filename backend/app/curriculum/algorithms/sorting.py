"""
Module: Sorting Algorithms and Asymptotic Complexity Analysis
Provides reference implementations, visualizations, and comparative benchmarks.
"""

import time
import random
from typing import List, TypeVar, Callable, Any, Tuple

T = TypeVar('T')


class SortingVisualizer:
    """Utility class to track comparison and swap operations in sorting algorithms."""

    def __init__(self) -> None:
        self.comparisons: int = 0
        self.swaps: int = 0
        self.history: List[List[Any]] = []

    def reset(self) -> None:
        self.comparisons = 0
        self.swaps = 0
        self.history.clear()

    def record_state(self, arr: List[Any]) -> None:
        self.history.append(list(arr))


class SortingSuite:
    """Comprehensive suite of classic and advanced sorting algorithms."""

    @staticmethod
    def bubble_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Bubble Sort implementation with early-termination optimization.
        Time Complexity: O(n^2) worst/average, O(n) best. Space: O(1).
        """
        items = list(arr)
        n = len(items)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if key(items[j]) > key(items[j + 1]):
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True
            if not swapped:
                break
        return items

    @staticmethod
    def insertion_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Insertion Sort implementation. Efficient for small or nearly sorted arrays.
        Time Complexity: O(n^2) worst, O(n) best. Space: O(1).
        """
        items = list(arr)
        for i in range(1, len(items)):
            current = items[i]
            j = i - 1
            while j >= 0 and key(items[j]) > key(current):
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = current
        return items

    @staticmethod
    def selection_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Selection Sort implementation. Minimizes number of writes.
        Time Complexity: O(n^2) for all cases. Space: O(1).
        """
        items = list(arr)
        n = len(items)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if key(items[j]) < key(items[min_idx]):
                    min_idx = j
            if min_idx != i:
                items[i], items[min_idx] = items[min_idx], items[i]
        return items

    @staticmethod
    def merge_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Merge Sort implementation (Divide-and-Conquer).
        Time Complexity: O(n log n) guaranteed. Space: O(n).
        """
        if len(arr) <= 1:
            return list(arr)

        mid = len(arr) // 2
        left = SortingSuite.merge_sort(arr[:mid], key=key)
        right = SortingSuite.merge_sort(arr[mid:], key=key)

        return SortingSuite._merge(left, right, key)

    @staticmethod
    def _merge(left: List[T], right: List[T], key: Callable[[T], Any]) -> List[T]:
        merged: List[T] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    @staticmethod
    def quick_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Quick Sort implementation using 3-way Dutch National Flag partitioning for duplicates.
        Time Complexity: O(n log n) average, O(n^2) worst. Space: O(log n).
        """
        items = list(arr)
        SortingSuite._quick_sort_recursive(items, 0, len(items) - 1, key)
        return items

    @staticmethod
    def _quick_sort_recursive(items: List[T], low: int, high: int, key: Callable[[T], Any]) -> None:
        if low >= high:
            return

        # Random pivot selection to prevent worst-case on sorted data
        pivot_idx = random.randint(low, high)
        items[low], items[pivot_idx] = items[pivot_idx], items[low]
        pivot_val = key(items[low])

        lt = low
        gt = high
        i = low + 1

        while i <= gt:
            val = key(items[i])
            if val < pivot_val:
                items[lt], items[i] = items[i], items[lt]
                lt += 1
                i += 1
            elif val > pivot_val:
                items[i], items[gt] = items[gt], items[i]
                gt -= 1
            else:
                i += 1

        SortingSuite._quick_sort_recursive(items, low, lt - 1, key)
        SortingSuite._quick_sort_recursive(items, gt + 1, high, key)

    @staticmethod
    def heap_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Heap Sort in-place using max-heap properties.
        Time Complexity: O(n log n). Space: O(1).
        """
        items = list(arr)
        n = len(items)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingSuite._heapify(items, n, i, key)

        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            items[i], items[0] = items[0], items[i]
            SortingSuite._heapify(items, i, 0, key)

        return items

    @staticmethod
    def _heapify(items: List[T], n: int, i: int, key: Callable[[T], Any]) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and key(items[left]) > key(items[largest]):
            largest = left
        if right < n and key(items[right]) > key(items[largest]):
            largest = right

        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            SortingSuite._heapify(items, n, largest, key)

    @staticmethod
    def radix_sort(arr: List[int]) -> List[int]:
        """
        Radix Sort for non-negative integers (LSD approach).
        Time Complexity: O(d * (n + b)) where d is digits, b is base. Space: O(n + b).
        """
        if not arr:
            return []
        items = list(arr)
        max_val = max(items)
        exp = 1
        while max_val // exp > 0:
            SortingSuite._counting_sort_by_digit(items, exp)
            exp *= 10
        return items

    @staticmethod
    def _counting_sort_by_digit(items: List[int], exp: int) -> None:
        n = len(items)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            idx = (items[i] // exp) % 10
            count[idx] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            idx = (items[i] // exp) % 10
            output[count[idx] - 1] = items[i]
            count[idx] -= 1

        for i in range(n):
            items[i] = output[i]

    @staticmethod
    def tim_sort(arr: List[T], key: Callable[[T], Any] = lambda x: x) -> List[T]:
        """
        Simplified TimSort combining Insertion Sort on small runs and Merge Sort.
        Time Complexity: O(n log n) worst/average, O(n) best. Space: O(n).
        """
        min_run = 32
        items = list(arr)
        n = len(items)

        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            # Sort individual runs using insertion sort
            for i in range(start + 1, end + 1):
                cur = items[i]
                j = i - 1
                while j >= start and key(items[j]) > key(cur):
                    items[j + 1] = items[j]
                    j -= 1
                items[j + 1] = cur

        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                if mid < right:
                    merged = SortingSuite._merge(items[left:mid + 1], items[mid + 1:right + 1], key)
                    items[left:left + len(merged)] = merged
            size *= 2

        return items


def benchmark_sorting_algorithms(size: int = 1000) -> dict:
    """Runs comparative benchmark across all sorting algorithms."""
    data = [random.randint(1, 10000) for _ in range(size)]
    results = {}

    algorithms = {
        "Bubble Sort": lambda: SortingSuite.bubble_sort(data),
        "Insertion Sort": lambda: SortingSuite.insertion_sort(data),
        "Selection Sort": lambda: SortingSuite.selection_sort(data),
        "Merge Sort": lambda: SortingSuite.merge_sort(data),
        "Quick Sort (3-Way)": lambda: SortingSuite.quick_sort(data),
        "Heap Sort": lambda: SortingSuite.heap_sort(data),
        "Radix Sort": lambda: SortingSuite.radix_sort(data),
        "TimSort": lambda: SortingSuite.tim_sort(data),
        "Python Built-in (Timsort)": lambda: sorted(data)
    }

    for name, func in algorithms.items():
        start = time.perf_counter()
        func()
        duration_ms = (time.perf_counter() - start) * 1000.0
        results[name] = round(duration_ms, 3)

    return results
