"""
Module: Graph Algorithms, Network Flows, and Shortest Paths
"""

import heapq
from collections import deque, defaultdict
from typing import Dict, List, Set, Tuple, Optional, Any, Generic, TypeVar

T = TypeVar('T')


class Graph(Generic[T]):
    """Adjacency List Graph representation supporting directed/undirected and weighted edges."""

    def __init__(self, directed: bool = False) -> None:
        self.directed: bool = directed
        self.adj_list: Dict[T, List[Tuple[T, float]]] = defaultdict(list)
        self.vertices: Set[T] = set()

    def add_vertex(self, v: T) -> None:
        self.vertices.add(v)
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u: T, v: T, weight: float = 1.0) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def get_neighbors(self, u: T) -> List[Tuple[T, float]]:
        return self.adj_list.get(u, [])


class GraphAlgorithms:
    """Collection of foundational and advanced graph traversal and pathfinding algorithms."""

    @staticmethod
    def bfs(graph: Graph[T], start: T) -> List[T]:
        """Breadth-First Search traversal visiting vertices layer by layer. Time: O(V + E)."""
        visited: Set[T] = {start}
        queue: deque = deque([start])
        traversal: List[T] = []

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor, _ in graph.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    @staticmethod
    def dfs(graph: Graph[T], start: T) -> List[T]:
        """Depth-First Search traversal exploring as deep as possible. Time: O(V + E)."""
        visited: Set[T] = set()
        traversal: List[T] = []

        def _dfs_visit(node: T) -> None:
            visited.add(node)
            traversal.append(node)
            for neighbor, _ in graph.get_neighbors(node):
                if neighbor not in visited:
                    _dfs_visit(neighbor)

        _dfs_visit(start)
        return traversal

    @staticmethod
    def dijkstra(graph: Graph[T], start: T) -> Tuple[Dict[T, float], Dict[T, Optional[T]]]:
        """
        Dijkstra's Single-Source Shortest Path algorithm using a priority queue (Min-Heap).
        Requires non-negative edge weights. Time: O((V + E) log V).
        """
        distances: Dict[T, float] = {v: float('inf') for v in graph.vertices}
        predecessors: Dict[T, Optional[T]] = {v: None for v in graph.vertices}
        distances[start] = 0.0

        pq: List[Tuple[float, T]] = [(0.0, start)]
        visited: Set[T] = set()

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for neighbor, weight in graph.get_neighbors(curr_node):
                if weight < 0:
                    raise ValueError("Dijkstra does not support negative edge weights. Use Bellman-Ford.")
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = curr_node
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances, predecessors

    @staticmethod
    def bellman_ford(graph: Graph[T], start: T) -> Tuple[Dict[T, float], bool]:
        """
        Bellman-Ford algorithm for shortest paths with negative weights and negative cycle detection.
        Time Complexity: O(V * E). Space: O(V).
        """
        distances: Dict[T, float] = {v: float('inf') for v in graph.vertices}
        distances[start] = 0.0

        v_count = len(graph.vertices)
        # Relax edges V - 1 times
        for _ in range(v_count - 1):
            for u in graph.vertices:
                if distances[u] == float('inf'):
                    continue
                for v, weight in graph.get_neighbors(u):
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # Check for negative cycles
        has_negative_cycle = False
        for u in graph.vertices:
            if distances[u] == float('inf'):
                continue
            for v, weight in graph.get_neighbors(u):
                if distances[u] + weight < distances[v]:
                    has_negative_cycle = True
                    break

        return distances, has_negative_cycle

    @staticmethod
    def topological_sort_kahn(graph: Graph[T]) -> List[T]:
        """
        Topological Sort of a Directed Acyclic Graph (DAG) using Kahn's Algorithm (In-degree queue).
        Time: O(V + E).
        """
        if not graph.directed:
            raise ValueError("Topological sort is only valid for directed graphs.")

        in_degree: Dict[T, int] = {v: 0 for v in graph.vertices}
        for u in graph.vertices:
            for v, _ in graph.get_neighbors(u):
                in_degree[v] += 1

        queue: deque = deque([v for v, deg in in_degree.items() if deg == 0])
        topo_order: List[T] = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor, _ in graph.get_neighbors(node):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != len(graph.vertices):
            raise ValueError("Graph contains a cycle! Topological sort not possible.")

        return topo_order

    @staticmethod
    def kruskal_mst(graph: Graph[T]) -> Tuple[List[Tuple[T, T, float]], float]:
        """
        Kruskal's Minimum Spanning Tree (MST) using Disjoint Set Union (DSU / Union-Find).
        Time Complexity: O(E log E).
        """
        edges: List[Tuple[float, T, T]] = []
        for u in graph.vertices:
            for v, w in graph.get_neighbors(u):
                if u < v or graph.directed:
                    edges.append((w, u, v))

        edges.sort()
        parent: Dict[T, T] = {v: v for v in graph.vertices}
        rank: Dict[T, int] = {v: 0 for v in graph.vertices}

        def find(i: T) -> T:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: T, j: T) -> bool:
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True

        mst_edges: List[Tuple[T, T, float]] = []
        total_weight: float = 0.0

        for weight, u, v in edges:
            if union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight

        return mst_edges, total_weight
