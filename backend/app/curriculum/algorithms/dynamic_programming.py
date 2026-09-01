"""
Module: Advanced Dynamic Programming Strategies & State Space Transitions
"""

from typing import List, Dict, Tuple, Any


class DPToolkit:
    """Classic Dynamic Programming problems with memoization and tabulation implementations."""

    @staticmethod
    def knapsack_01(values: List[int], weights: List[int], capacity: int) -> Tuple[int, List[int]]:
        """
        0/1 Knapsack problem using 2D DP Table.
        Returns maximum profit and indices of selected items.
        """
        n = len(values)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            val = values[i - 1]
            wt = weights[i - 1]
            for w in range(capacity + 1):
                if wt <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt] + val)
                else:
                    dp[i][w] = dp[i - 1][w]

        # Backtrack to identify selected items
        selected: List[int] = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected.append(i - 1)
                w -= weights[i - 1]

        return dp[n][capacity], selected

    @staticmethod
    def longest_common_subsequence(s1: str, s2: str) -> Tuple[int, str]:
        """
        Computes the length and reconstructed string of the Longest Common Subsequence (LCS).
        """
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct LCS string
        chars: List[str] = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                chars.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return dp[m][n], "".join(reversed(chars))

    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """
        Levenshtein Edit Distance (Insert, Delete, Replace).
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # Deletion
                        dp[i][j - 1],      # Insertion
                        dp[i - 1][j - 1]   # Replacement
                    )

        return dp[m][n]

    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """
        Finds the fewest number of coins needed to make up that amount.
        Returns -1 if that amount of money cannot be made up.
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return int(dp[amount]) if dp[amount] != float('inf') else -1
