"""
Module: Distributed Systems, Consistent Hashing, and Consensus Simulation
"""

import hashlib
import bisect
from typing import List, Dict, Optional, Any, Set


class ConsistentHashRing:
    """
    Consistent Hashing with Virtual Nodes for distributed cache/database sharding.
    Ensures minimal keys remapped when nodes join or leave.
    """

    def __init__(self, replicas: int = 100) -> None:
        self.replicas = replicas
        self.ring: Dict[int, str] = {}
        self.sorted_keys: List[int] = []
        self.nodes: Set[str] = set()

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        self.nodes.add(node)
        for i in range(self.replicas):
            virtual_key = f"{node}#vnode{i}"
            h = self._hash(virtual_key)
            self.ring[h] = node
            bisect.insort(self.sorted_keys, h)

    def remove_node(self, node: str) -> None:
        if node not in self.nodes:
            return
        self.nodes.remove(node)
        for i in range(self.replicas):
            virtual_key = f"{node}#vnode{i}"
            h = self._hash(virtual_key)
            if h in self.ring:
                del self.ring[h]
                idx = bisect.bisect_left(self.sorted_keys, h)
                if idx < len(self.sorted_keys) and self.sorted_keys[idx] == h:
                    self.sorted_keys.pop(idx)

    def get_node(self, key: str) -> Optional[str]:
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.sorted_keys, h)
        if idx == len(self.sorted_keys):
            idx = 0
        return self.ring[self.sorted_keys[idx]]


class VectorClock:
    """Vector Clock for tracking causal order of events in distributed state machines."""

    def __init__(self, node_id: str) -> None:
        self.node_id = node_id
        self.clock: Dict[str, int] = {node_id: 0}

    def increment(self) -> None:
        self.clock[self.node_id] = self.clock.get(self.node_id, 0) + 1

    def send_event(self) -> Dict[str, int]:
        self.increment()
        return dict(self.clock)

    def receive_event(self, incoming_clock: Dict[str, int]) -> None:
        for node, time_val in incoming_clock.items():
            self.clock[node] = max(self.clock.get(node, 0), time_val)
        self.increment()

    def compare(self, other_clock: Dict[str, int]) -> str:
        """
        Returns 'before', 'after', 'equal', or 'concurrent'.
        """
        greater = False
        lesser = False
        all_nodes = set(self.clock.keys()).union(set(other_clock.keys()))

        for n in all_nodes:
            t1 = self.clock.get(n, 0)
            t2 = other_clock.get(n, 0)
            if t1 > t2:
                greater = True
            elif t1 < t2:
                lesser = True

        if greater and not lesser:
            return 'after'
        elif lesser and not greater:
            return 'before'
        elif not greater and not lesser:
            return 'equal'
        else:
            return 'concurrent'
