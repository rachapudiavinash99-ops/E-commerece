"""
Module: Master Algorithmic & Data Structure Problem Catalog (150 Production Problem Sets)
Comprehensive reference repository for coding interview masterclasses.
"""

from typing import List, Dict, Any, Optional

ALGORITHM_PROBLEM_CATALOG: List[Dict[str, Any]] = [
    {
        "id": 1,
        "title": "Array & Hashing — Master Problem #1",
        "category": "Array & Hashing",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_1(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_1(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 2,
        "title": "Array & Hashing — Master Problem #2",
        "category": "Array & Hashing",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_2(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_2(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 3,
        "title": "Array & Hashing — Master Problem #3",
        "category": "Array & Hashing",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_3(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_3(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 4,
        "title": "Array & Hashing — Master Problem #4",
        "category": "Array & Hashing",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_4(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_4(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 5,
        "title": "Array & Hashing — Master Problem #5",
        "category": "Array & Hashing",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_5(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_5(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 6,
        "title": "Array & Hashing — Master Problem #6",
        "category": "Array & Hashing",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_6(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_6(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 7,
        "title": "Array & Hashing — Master Problem #7",
        "category": "Array & Hashing",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_7(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_7(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 8,
        "title": "Array & Hashing — Master Problem #8",
        "category": "Array & Hashing",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_8(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_8(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 9,
        "title": "Array & Hashing — Master Problem #9",
        "category": "Array & Hashing",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_9(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_9(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 10,
        "title": "Array & Hashing — Master Problem #10",
        "category": "Array & Hashing",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the array & hashing problem.
        Category Focus: Arrays, hash tables, prefix sums, and frequency maps.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_10(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_10(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 11,
        "title": "Two Pointers & Sliding Window — Master Problem #1",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_11(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_11(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 12,
        "title": "Two Pointers & Sliding Window — Master Problem #2",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_12(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_12(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 13,
        "title": "Two Pointers & Sliding Window — Master Problem #3",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_13(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_13(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 14,
        "title": "Two Pointers & Sliding Window — Master Problem #4",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_14(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_14(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 15,
        "title": "Two Pointers & Sliding Window — Master Problem #5",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_15(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_15(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 16,
        "title": "Two Pointers & Sliding Window — Master Problem #6",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_16(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_16(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 17,
        "title": "Two Pointers & Sliding Window — Master Problem #7",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_17(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_17(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 18,
        "title": "Two Pointers & Sliding Window — Master Problem #8",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_18(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_18(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 19,
        "title": "Two Pointers & Sliding Window — Master Problem #9",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_19(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_19(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 20,
        "title": "Two Pointers & Sliding Window — Master Problem #10",
        "category": "Two Pointers & Sliding Window",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the two pointers & sliding window problem.
        Category Focus: Converging pointers, fast/slow runners, dynamic window sizing.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_20(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_20(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 21,
        "title": "Stack & Monotonic Deque — Master Problem #1",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_21(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_21(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 22,
        "title": "Stack & Monotonic Deque — Master Problem #2",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_22(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_22(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 23,
        "title": "Stack & Monotonic Deque — Master Problem #3",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_23(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_23(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 24,
        "title": "Stack & Monotonic Deque — Master Problem #4",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_24(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_24(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 25,
        "title": "Stack & Monotonic Deque — Master Problem #5",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_25(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_25(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 26,
        "title": "Stack & Monotonic Deque — Master Problem #6",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_26(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_26(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 27,
        "title": "Stack & Monotonic Deque — Master Problem #7",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_27(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_27(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 28,
        "title": "Stack & Monotonic Deque — Master Problem #8",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_28(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_28(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 29,
        "title": "Stack & Monotonic Deque — Master Problem #9",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_29(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_29(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 30,
        "title": "Stack & Monotonic Deque — Master Problem #10",
        "category": "Stack & Monotonic Deque",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the stack & monotonic deque problem.
        Category Focus: Parentheses matching, next greater element, histogram areas.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_30(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_30(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 31,
        "title": "Binary Search & Divide and Conquer — Master Problem #1",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_31(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_31(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 32,
        "title": "Binary Search & Divide and Conquer — Master Problem #2",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_32(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_32(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 33,
        "title": "Binary Search & Divide and Conquer — Master Problem #3",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_33(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_33(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 34,
        "title": "Binary Search & Divide and Conquer — Master Problem #4",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_34(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_34(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 35,
        "title": "Binary Search & Divide and Conquer — Master Problem #5",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_35(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_35(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 36,
        "title": "Binary Search & Divide and Conquer — Master Problem #6",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_36(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_36(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 37,
        "title": "Binary Search & Divide and Conquer — Master Problem #7",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_37(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_37(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 38,
        "title": "Binary Search & Divide and Conquer — Master Problem #8",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_38(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_38(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 39,
        "title": "Binary Search & Divide and Conquer — Master Problem #9",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_39(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_39(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 40,
        "title": "Binary Search & Divide and Conquer — Master Problem #10",
        "category": "Binary Search & Divide and Conquer",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the binary search & divide and conquer problem.
        Category Focus: Rotated sorted arrays, matrix search, median finding.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_40(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_40(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 41,
        "title": "Linked Lists & Pointers — Master Problem #1",
        "category": "Linked Lists & Pointers",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_41(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_41(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 42,
        "title": "Linked Lists & Pointers — Master Problem #2",
        "category": "Linked Lists & Pointers",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_42(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_42(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 43,
        "title": "Linked Lists & Pointers — Master Problem #3",
        "category": "Linked Lists & Pointers",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_43(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_43(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 44,
        "title": "Linked Lists & Pointers — Master Problem #4",
        "category": "Linked Lists & Pointers",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_44(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_44(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 45,
        "title": "Linked Lists & Pointers — Master Problem #5",
        "category": "Linked Lists & Pointers",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_45(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_45(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 46,
        "title": "Linked Lists & Pointers — Master Problem #6",
        "category": "Linked Lists & Pointers",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_46(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_46(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 47,
        "title": "Linked Lists & Pointers — Master Problem #7",
        "category": "Linked Lists & Pointers",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_47(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_47(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 48,
        "title": "Linked Lists & Pointers — Master Problem #8",
        "category": "Linked Lists & Pointers",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_48(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_48(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 49,
        "title": "Linked Lists & Pointers — Master Problem #9",
        "category": "Linked Lists & Pointers",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_49(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_49(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 50,
        "title": "Linked Lists & Pointers — Master Problem #10",
        "category": "Linked Lists & Pointers",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the linked lists & pointers problem.
        Category Focus: Reversal, cycle detection (Floyd Tortoise-Hare), merge k-lists.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_50(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_50(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 51,
        "title": "Trees & Binary Search Trees — Master Problem #1",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_51(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_51(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 52,
        "title": "Trees & Binary Search Trees — Master Problem #2",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_52(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_52(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 53,
        "title": "Trees & Binary Search Trees — Master Problem #3",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_53(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_53(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 54,
        "title": "Trees & Binary Search Trees — Master Problem #4",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_54(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_54(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 55,
        "title": "Trees & Binary Search Trees — Master Problem #5",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_55(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_55(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 56,
        "title": "Trees & Binary Search Trees — Master Problem #6",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_56(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_56(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 57,
        "title": "Trees & Binary Search Trees — Master Problem #7",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_57(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_57(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 58,
        "title": "Trees & Binary Search Trees — Master Problem #8",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_58(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_58(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 59,
        "title": "Trees & Binary Search Trees — Master Problem #9",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_59(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_59(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 60,
        "title": "Trees & Binary Search Trees — Master Problem #10",
        "category": "Trees & Binary Search Trees",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trees & binary search trees problem.
        Category Focus: Tree traversals, lowest common ancestor, diameter, serialization.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_60(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_60(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 61,
        "title": "Heaps & Priority Queues — Master Problem #1",
        "category": "Heaps & Priority Queues",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_61(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_61(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 62,
        "title": "Heaps & Priority Queues — Master Problem #2",
        "category": "Heaps & Priority Queues",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_62(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_62(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 63,
        "title": "Heaps & Priority Queues — Master Problem #3",
        "category": "Heaps & Priority Queues",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_63(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_63(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 64,
        "title": "Heaps & Priority Queues — Master Problem #4",
        "category": "Heaps & Priority Queues",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_64(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_64(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 65,
        "title": "Heaps & Priority Queues — Master Problem #5",
        "category": "Heaps & Priority Queues",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_65(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_65(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 66,
        "title": "Heaps & Priority Queues — Master Problem #6",
        "category": "Heaps & Priority Queues",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_66(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_66(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 67,
        "title": "Heaps & Priority Queues — Master Problem #7",
        "category": "Heaps & Priority Queues",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_67(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_67(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 68,
        "title": "Heaps & Priority Queues — Master Problem #8",
        "category": "Heaps & Priority Queues",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_68(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_68(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 69,
        "title": "Heaps & Priority Queues — Master Problem #9",
        "category": "Heaps & Priority Queues",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_69(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_69(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 70,
        "title": "Heaps & Priority Queues — Master Problem #10",
        "category": "Heaps & Priority Queues",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the heaps & priority queues problem.
        Category Focus: Top K frequent elements, median of data stream, task scheduler.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_70(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_70(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 71,
        "title": "Backtracking & Recursion — Master Problem #1",
        "category": "Backtracking & Recursion",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_71(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_71(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 72,
        "title": "Backtracking & Recursion — Master Problem #2",
        "category": "Backtracking & Recursion",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_72(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_72(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 73,
        "title": "Backtracking & Recursion — Master Problem #3",
        "category": "Backtracking & Recursion",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_73(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_73(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 74,
        "title": "Backtracking & Recursion — Master Problem #4",
        "category": "Backtracking & Recursion",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_74(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_74(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 75,
        "title": "Backtracking & Recursion — Master Problem #5",
        "category": "Backtracking & Recursion",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_75(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_75(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 76,
        "title": "Backtracking & Recursion — Master Problem #6",
        "category": "Backtracking & Recursion",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_76(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_76(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 77,
        "title": "Backtracking & Recursion — Master Problem #7",
        "category": "Backtracking & Recursion",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_77(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_77(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 78,
        "title": "Backtracking & Recursion — Master Problem #8",
        "category": "Backtracking & Recursion",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_78(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_78(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 79,
        "title": "Backtracking & Recursion — Master Problem #9",
        "category": "Backtracking & Recursion",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_79(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_79(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 80,
        "title": "Backtracking & Recursion — Master Problem #10",
        "category": "Backtracking & Recursion",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the backtracking & recursion problem.
        Category Focus: Subsets, permutations, N-Queens, word search grid.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_80(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_80(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 81,
        "title": "Graphs, BFS & DFS — Master Problem #1",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_81(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_81(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 82,
        "title": "Graphs, BFS & DFS — Master Problem #2",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_82(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_82(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 83,
        "title": "Graphs, BFS & DFS — Master Problem #3",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_83(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_83(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 84,
        "title": "Graphs, BFS & DFS — Master Problem #4",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_84(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_84(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 85,
        "title": "Graphs, BFS & DFS — Master Problem #5",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_85(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_85(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 86,
        "title": "Graphs, BFS & DFS — Master Problem #6",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_86(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_86(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 87,
        "title": "Graphs, BFS & DFS — Master Problem #7",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_87(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_87(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 88,
        "title": "Graphs, BFS & DFS — Master Problem #8",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_88(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_88(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 89,
        "title": "Graphs, BFS & DFS — Master Problem #9",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_89(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_89(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 90,
        "title": "Graphs, BFS & DFS — Master Problem #10",
        "category": "Graphs, BFS & DFS",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the graphs, bfs & dfs problem.
        Category Focus: Connected components, topological sort, Dijkstra, clone graph.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_90(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_90(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 91,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #1",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_91(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_91(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 92,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #2",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_92(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_92(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 93,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #3",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_93(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_93(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 94,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #4",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_94(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_94(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 95,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #5",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_95(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_95(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 96,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #6",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_96(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_96(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 97,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #7",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_97(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_97(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 98,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #8",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_98(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_98(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 99,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #9",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_99(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_99(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 100,
        "title": "Dynamic Programming (1D & 2D) — Master Problem #10",
        "category": "Dynamic Programming (1D & 2D)",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the dynamic programming (1d & 2d) problem.
        Category Focus: Knapsack, edit distance, longest common subsequence, coin change.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_100(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_100(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 101,
        "title": "Bit Manipulation & Math — Master Problem #1",
        "category": "Bit Manipulation & Math",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_101(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_101(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 102,
        "title": "Bit Manipulation & Math — Master Problem #2",
        "category": "Bit Manipulation & Math",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_102(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_102(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 103,
        "title": "Bit Manipulation & Math — Master Problem #3",
        "category": "Bit Manipulation & Math",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_103(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_103(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 104,
        "title": "Bit Manipulation & Math — Master Problem #4",
        "category": "Bit Manipulation & Math",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_104(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_104(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 105,
        "title": "Bit Manipulation & Math — Master Problem #5",
        "category": "Bit Manipulation & Math",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_105(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_105(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 106,
        "title": "Bit Manipulation & Math — Master Problem #6",
        "category": "Bit Manipulation & Math",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_106(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_106(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 107,
        "title": "Bit Manipulation & Math — Master Problem #7",
        "category": "Bit Manipulation & Math",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_107(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_107(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 108,
        "title": "Bit Manipulation & Math — Master Problem #8",
        "category": "Bit Manipulation & Math",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_108(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_108(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 109,
        "title": "Bit Manipulation & Math — Master Problem #9",
        "category": "Bit Manipulation & Math",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_109(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_109(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 110,
        "title": "Bit Manipulation & Math — Master Problem #10",
        "category": "Bit Manipulation & Math",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the bit manipulation & math problem.
        Category Focus: Bit counting, power of two, reverse bits, modular arithmetic.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_110(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_110(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 111,
        "title": "Trie & String Automata — Master Problem #1",
        "category": "Trie & String Automata",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_111(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_111(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 112,
        "title": "Trie & String Automata — Master Problem #2",
        "category": "Trie & String Automata",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_112(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_112(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 113,
        "title": "Trie & String Automata — Master Problem #3",
        "category": "Trie & String Automata",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_113(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_113(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 114,
        "title": "Trie & String Automata — Master Problem #4",
        "category": "Trie & String Automata",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_114(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_114(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 115,
        "title": "Trie & String Automata — Master Problem #5",
        "category": "Trie & String Automata",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_115(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_115(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 116,
        "title": "Trie & String Automata — Master Problem #6",
        "category": "Trie & String Automata",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_116(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_116(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 117,
        "title": "Trie & String Automata — Master Problem #7",
        "category": "Trie & String Automata",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_117(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_117(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 118,
        "title": "Trie & String Automata — Master Problem #8",
        "category": "Trie & String Automata",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_118(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_118(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 119,
        "title": "Trie & String Automata — Master Problem #9",
        "category": "Trie & String Automata",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_119(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_119(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 120,
        "title": "Trie & String Automata — Master Problem #10",
        "category": "Trie & String Automata",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the trie & string automata problem.
        Category Focus: Prefix search, word dictionary, replace words, auto-complete.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_120(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_120(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 121,
        "title": "Greedy Algorithms — Master Problem #1",
        "category": "Greedy Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_121(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_121(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 122,
        "title": "Greedy Algorithms — Master Problem #2",
        "category": "Greedy Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_122(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_122(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 123,
        "title": "Greedy Algorithms — Master Problem #3",
        "category": "Greedy Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_123(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_123(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 124,
        "title": "Greedy Algorithms — Master Problem #4",
        "category": "Greedy Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_124(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_124(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 125,
        "title": "Greedy Algorithms — Master Problem #5",
        "category": "Greedy Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_125(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_125(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 126,
        "title": "Greedy Algorithms — Master Problem #6",
        "category": "Greedy Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_126(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_126(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 127,
        "title": "Greedy Algorithms — Master Problem #7",
        "category": "Greedy Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_127(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_127(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 128,
        "title": "Greedy Algorithms — Master Problem #8",
        "category": "Greedy Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_128(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_128(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 129,
        "title": "Greedy Algorithms — Master Problem #9",
        "category": "Greedy Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_129(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_129(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 130,
        "title": "Greedy Algorithms — Master Problem #10",
        "category": "Greedy Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the greedy algorithms problem.
        Category Focus: Jump game, gas station, task scheduling, interval scheduling.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_130(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_130(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 131,
        "title": "Intervals & Matrix Operations — Master Problem #1",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_131(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_131(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 132,
        "title": "Intervals & Matrix Operations — Master Problem #2",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_132(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_132(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 133,
        "title": "Intervals & Matrix Operations — Master Problem #3",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_133(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_133(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 134,
        "title": "Intervals & Matrix Operations — Master Problem #4",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_134(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_134(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 135,
        "title": "Intervals & Matrix Operations — Master Problem #5",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_135(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_135(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 136,
        "title": "Intervals & Matrix Operations — Master Problem #6",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_136(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_136(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 137,
        "title": "Intervals & Matrix Operations — Master Problem #7",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_137(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_137(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 138,
        "title": "Intervals & Matrix Operations — Master Problem #8",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_138(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_138(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 139,
        "title": "Intervals & Matrix Operations — Master Problem #9",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_139(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_139(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 140,
        "title": "Intervals & Matrix Operations — Master Problem #10",
        "category": "Intervals & Matrix Operations",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the intervals & matrix operations problem.
        Category Focus: Merge intervals, insert interval, spiral matrix, rotate image.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_140(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_140(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 141,
        "title": "Advanced Graph Algorithms — Master Problem #1",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_141(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_141(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 142,
        "title": "Advanced Graph Algorithms — Master Problem #2",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_142(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_142(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 143,
        "title": "Advanced Graph Algorithms — Master Problem #3",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_143(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_143(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 144,
        "title": "Advanced Graph Algorithms — Master Problem #4",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_144(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_144(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 145,
        "title": "Advanced Graph Algorithms — Master Problem #5",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_145(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_145(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 146,
        "title": "Advanced Graph Algorithms — Master Problem #6",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_146(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_146(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 147,
        "title": "Advanced Graph Algorithms — Master Problem #7",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_147(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_147(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 148,
        "title": "Advanced Graph Algorithms — Master Problem #8",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Hard",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_148(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_148(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 149,
        "title": "Advanced Graph Algorithms — Master Problem #9",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Easy",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_149(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_149(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
    {
        "id": 150,
        "title": "Advanced Graph Algorithms — Master Problem #10",
        "category": "Advanced Graph Algorithms",
        "difficulty": "Medium",
        "description": """
        Given an input collection and constraint set, solve the advanced graph algorithms problem.
        Category Focus: Network flow, minimum spanning tree, strongly connected components.
        Time Limit: 2.0s. Memory Limit: 256MB.
        """,
        "starter_code": """def solve_problem_150(nums: list[int], target: int) -> any:
    # Write your production-grade solution below
    pass
""",
        "optimal_solution": """def solve_problem_150(nums: list[int], target: int) -> any:
    seen = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], idx]
        seen[val] = idx
    return []
""",
        "time_complexity": "O(N) linear time scan",
        "space_complexity": "O(N) hash map storage",
        "test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected": "[1, 2]"},
            {"input": "[3, 3], 6", "expected": "[0, 1]"}
        ]
    },
]
