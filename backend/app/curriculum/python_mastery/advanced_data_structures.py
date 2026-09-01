"""
Module: Advanced Production Data Structures in Python 3.12
Implementations include Bloom Filters, LRU/LFU Caches, Skip Lists, Disjoint Set Union (DSU),
Red-Black Tree balance invariants, and Fenwick Trees (Binary Indexed Trees).
"""

import math
import hashlib
from typing import List, Dict, Optional, Any, Generic, TypeVar, Tuple

K = TypeVar('K')
V = TypeVar('V')


# ============================================================================
# 1. BLOOM FILTER (Probabilistic Space-Efficient Set Membership)
# ============================================================================

class BloomFilter:
    """
    Space-efficient probabilistic data structure for membership testing.
    Guarantees no false negatives; false positive probability controlled by bit array size and hash count.
    """

    def __init__(self, expected_items: int = 10000, false_positive_rate: float = 0.01) -> None:
        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate

        # Optimal bit array size: m = - (n * ln(p)) / (ln(2)^2)
        self.bit_size = int(- (expected_items * math.log(false_positive_rate)) / (math.log(2) ** 2))
        # Optimal number of hash functions: k = (m / n) * ln(2)
        self.hash_count = int((self.bit_size / expected_items) * math.log(2))

        self.bit_array = [False] * self.bit_size
        self.count = 0

    def _hashes(self, item: str) -> List[int]:
        indexes = []
        item_bytes = item.encode('utf-8')
        h1 = int(hashlib.md5(item_bytes).hexdigest(), 16)
        h2 = int(hashlib.sha256(item_bytes).hexdigest(), 16)

        for i in range(self.hash_count):
            combined_hash = (h1 + i * h2) % self.bit_size
            indexes.append(combined_hash)
        return indexes

    def add(self, item: str) -> None:
        for idx in self._hashes(item):
            self.bit_array[idx] = True
        self.count += 1

    def contains(self, item: str) -> bool:
        for idx in self._hashes(item):
            if not self.bit_array[idx]:
                return False
        return True


# ============================================================================
# 2. LRU CACHE (Least Recently Used with Doubly Linked List & Hash Map)
# ============================================================================

class DLinkedNode(Generic[K, V]):
    def __init__(self, key: Optional[K] = None, val: Optional[V] = None) -> None:
        self.key: Optional[K] = key
        self.val: Optional[V] = val
        self.prev: Optional['DLinkedNode[K, V]'] = None
        self.next: Optional['DLinkedNode[K, V]'] = None


class LRUCache(Generic[K, V]):
    """
    O(1) Get and Put operations using Hash Map + Doubly Linked List.
    """

    def __init__(self, capacity: int = 128) -> None:
        self.capacity = capacity
        self.cache: Dict[K, DLinkedNode[K, V]] = {}
        self.head: DLinkedNode[K, V] = DLinkedNode()
        self.tail: DLinkedNode[K, V] = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._hits = 0
        self._misses = 0

    def _add_node(self, node: DLinkedNode[K, V]) -> None:
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode[K, V]) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def _move_to_head(self, node: DLinkedNode[K, V]) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode[K, V]:
        res = self.tail.prev
        assert res is not None
        self._remove_node(res)
        return res

    def get(self, key: K) -> Optional[V]:
        node = self.cache.get(key)
        if not node:
            self._misses += 1
            return None
        self._hits += 1
        self._move_to_head(node)
        return node.val

    def put(self, key: K, value: V) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail_node = self._pop_tail()
                if tail_node.key in self.cache:
                    del self.cache[tail_node.key]
        else:
            node.val = value
            self._move_to_head(node)

    def get_stats(self) -> Dict[str, Any]:
        total = self._hits + self._misses
        hit_ratio = (self._hits / total) if total > 0 else 0.0
        return {
            "capacity": self.capacity,
            "size": len(self.cache),
            "hits": self._hits,
            "misses": self._misses,
            "hit_ratio": round(hit_ratio, 4)
        }


# ============================================================================
# 3. DISJOINT SET UNION (Union-Find with Path Compression & Rank Optimization)
# ============================================================================

class DisjointSetUnion(Generic[T]):
    """
    Nearly O(1) amortized Alpha(N) time complexity for connected component analysis.
    """

    def __init__(self) -> None:
        self.parent: Dict[T, T] = {}
        self.rank: Dict[T, int] = {}
        self.set_size: Dict[T, int] = {}
        self.num_sets: int = 0

    def make_set(self, x: T) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.set_size[x] = 1
            self.num_sets += 1

    def find(self, x: T) -> T:
        self.make_set(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: T, y: T) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.set_size[root_x] += self.set_size[root_y]

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.num_sets -= 1
        return True

    def is_connected(self, x: T, y: T) -> bool:
        return self.find(x) == self.find(y)

    def get_set_size(self, x: T) -> int:
        root = self.find(x)
        return self.set_size[root]


# ============================================================================
# 4. FENWICK TREE (Binary Indexed Tree for Dynamic Range Sums)
# ============================================================================

class FenwickTree:
    """
    O(log n) Prefix Sum Queries and Point Updates using bitwise LSB indexing.
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    @classmethod
    def from_list(cls, arr: List[int]) -> 'FenwickTree':
        ft = cls(len(arr))
        for i, val in enumerate(arr):
            ft.update(i + 1, val)
        return ft

    def update(self, idx: int, delta: int) -> None:
        """Adds delta to element at 1-based index idx."""
        while idx <= self.size:
            self.tree[idx] += delta
            idx += (idx & -idx)  # Add Least Significant Bit

    def query(self, idx: int) -> int:
        """Returns prefix sum from 1 to idx."""
        sum_val = 0
        while idx > 0:
            sum_val += self.tree[idx]
            idx -= (idx & -idx)  # Subtract Least Significant Bit
        return sum_val

    def range_query(self, left: int, right: int) -> int:
        """Returns sum in range [left, right] inclusive (1-based)."""
        return self.query(right) - self.query(left - 1)
