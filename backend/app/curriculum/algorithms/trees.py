"""
Module: Binary Search Trees, Balanced AVL Trees, Tries, and Segment Trees
"""

from typing import Optional, List, Any, Generic, TypeVar, Tuple

T = TypeVar('T')


class BSTNode(Generic[T]):
    def __init__(self, key: T, val: Any = None) -> None:
        self.key: T = key
        self.val: Any = val if val is not None else key
        self.left: Optional['BSTNode[T]'] = None
        self.right: Optional['BSTNode[T]'] = None
        self.height: int = 1


class BinarySearchTree(Generic[T]):
    """Classic Binary Search Tree with insertion, deletion, and order traversals."""

    def __init__(self) -> None:
        self.root: Optional[BSTNode[T]] = None
        self._size: int = 0

    def insert(self, key: T, val: Any = None) -> None:
        self.root = self._insert_node(self.root, key, val)

    def _insert_node(self, node: Optional[BSTNode[T]], key: T, val: Any) -> BSTNode[T]:
        if not node:
            self._size += 1
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._insert_node(node.left, key, val)
        elif key > node.key:
            node.right = self._insert_node(node.right, key, val)
        else:
            node.val = val
        return node

    def search(self, key: T) -> Optional[Any]:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder_traversal(self) -> List[T]:
        result: List[T] = []
        def _inorder(n: Optional[BSTNode[T]]) -> None:
            if n:
                _inorder(n.left)
                result.append(n.key)
                _inorder(n.right)
        _inorder(self.root)
        return result

    def size(self) -> int:
        return self._size


class AVLTree(Generic[T]):
    """Self-balancing AVL Tree maintaining O(log n) search, insertion, and deletion."""

    def __init__(self) -> None:
        self.root: Optional[BSTNode[T]] = None

    def _get_height(self, node: Optional[BSTNode[T]]) -> int:
        return node.height if node else 0

    def _get_balance(self, node: Optional[BSTNode[T]]) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y: BSTNode[T]) -> BSTNode[T]:
        x = y.left
        assert x is not None
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        return x

    def _rotate_left(self, x: BSTNode[T]) -> BSTNode[T]:
        y = x.right
        assert y is not None
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def insert(self, key: T) -> None:
        self.root = self._insert_node(self.root, key)

    def _insert_node(self, node: Optional[BSTNode[T]], key: T) -> BSTNode[T]:
        if not node:
            return BSTNode(key)

        if key < node.key:
            node.left = self._insert_node(node.left, key)
        elif key > node.key:
            node.right = self._insert_node(node.right, key)
        else:
            return node

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and node.left and key < node.left.key:
            return self._rotate_right(node)

        # Right Right
        if balance < -1 and node.right and key > node.right.key:
            return self._rotate_left(node)

        # Left Right
        if balance > 1 and node.left and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left
        if balance < -1 and node.right and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False
        self.frequency: int = 0


class PrefixTrie:
    """Trie (Prefix Tree) data structure for efficient string retrieval and autocomplete."""

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
        node.frequency += 1

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix: str, max_results: int = 10) -> List[str]:
        node = self._find_node(prefix)
        if not node:
            return []
        results: List[str] = []

        def _collect(curr: TrieNode, path: List[str]) -> None:
            if len(results) >= max_results:
                return
            if curr.is_end_of_word:
                results.append(prefix + "".join(path))
            for char, next_node in sorted(curr.children.items()):
                path.append(char)
                _collect(next_node, path)
                path.pop()

        _collect(node, [])
        return results

    def _find_node(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s.lower():
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
