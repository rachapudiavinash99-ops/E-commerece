"""
Module: Advanced String Algorithms, Pattern Matching, and Automata
Covers KMP (Knuth-Morris-Pratt), Rabin-Karp Rolling Hash, Z-Algorithm, and Manacher's Algorithm.
"""

from typing import List, Tuple, Dict, Optional


class StringAlgorithms:
    """Production-grade string matching and palindrome pattern recognition."""

    @staticmethod
    def kmp_search(text: str, pattern: str) -> List[int]:
        """
        Knuth-Morris-Pratt (KMP) exact pattern matching using Longest Prefix Suffix (LPS) array.
        Time Complexity: O(N + M) guaranteed. Space: O(M).
        """
        if not pattern or not text or len(pattern) > len(text):
            return []

        # 1. Compute LPS table
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # 2. Search pattern in text
        n = len(text)
        matches: List[int] = []
        i = j = 0

        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return matches

    @staticmethod
    def rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
        """
        Rabin-Karp Rolling Hash string search algorithm.
        Average Time: O(N + M), Worst: O(N * M).
        """
        if not pattern or not text or len(pattern) > len(text):
            return []

        d = 256  # Alphabet size
        m = len(pattern)
        n = len(text)
        p_hash = 0
        t_hash = 0
        h = 1
        matches: List[int] = []

        # The value of h would be "pow(d, m-1)%prime"
        for _ in range(m - 1):
            h = (h * d) % prime

        # Calculate initial hash of pattern and first window
        for i in range(m):
            p_hash = (d * p_hash + ord(pattern[i])) % prime
            t_hash = (d * t_hash + ord(text[i])) % prime

        # Slide pattern over text
        for i in range(n - m + 1):
            if p_hash == t_hash:
                # Character by character check on hash match
                if text[i:i + m] == pattern:
                    matches.append(i)

            # Compute hash for next window
            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
                if t_hash < 0:
                    t_hash += prime

        return matches

    @staticmethod
    def z_algorithm(text: str) -> List[int]:
        """
        Computes the Z-Array where Z[i] is the length of longest common prefix between text and text[i:].
        Time Complexity: O(N).
        """
        n = len(text)
        z = [0] * n
        l, r, k = 0, 0, 0

        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and text[r - l] == text[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and text[r - l] == text[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1

        return z

    @staticmethod
    def manacher_longest_palindrome(s: str) -> str:
        """
        Manacher's Algorithm for finding the longest palindromic substring in linear O(N) time.
        """
        if not s:
            return ""

        # Transform string to handle odd and even palindromes: "aba" -> "^#a#b#a#$"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        c = 0
        r = 0

        for i in range(1, n - 1):
            i_mirror = 2 * c - i
            if r > i:
                p[i] = min(r - i, p[i_mirror])
            else:
                p[i] = 0

            # Expand around center i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > r:
                c = i
                r = i + p[i]

        max_len, center_idx = max((n, i) for i, n in enumerate(p))
        start = (center_idx - max_len) // 2
        return s[start:start + max_len]
