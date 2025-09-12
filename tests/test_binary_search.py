import sys
from pathlib import Path

import pytest

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from binary_search import Solution


class TestBinarySearch:
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()

    def test_binary_search_exists_middle(self, solution: Solution) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 7)
        if not result:
            raise ValueError("Should find middle element 7")

    def test_binary_search_exists_first(self, solution: Solution) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 1)
        if not result:
            raise ValueError("Should find first element 1")

    def test_binary_search_exists_last(self, solution: Solution) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 13)
        if not result:
            raise ValueError("Should find last element 13")

    def test_binary_search_not_exists(self, solution: Solution) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 6)
        if result:
            raise ValueError("Should not find non-existent element 6")

    def test_binary_search_not_exists_out_of_range_low(
        self,
        solution: Solution,
    ) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 0)
        if result:
            raise ValueError("Should not find element below range 0")

    def test_binary_search_not_exists_out_of_range_high(
        self,
        solution: Solution,
    ) -> None:
        haystack = [1, 3, 5, 7, 9, 11, 13]
        result = solution.binary_search(haystack, 15)
        if result:
            raise ValueError("Should not find element above range 15")

    def test_binary_search_empty_array(self, solution: Solution) -> None:
        haystack: list[int] = []
        result = solution.binary_search(haystack, 5)
        if result:
            raise ValueError("Should not find anything in empty array")

    def test_binary_search_single_element_exists(self, solution: Solution) -> None:
        haystack = [42]
        result = solution.binary_search(haystack, 42)
        if not result:
            raise ValueError("Should find single element 42")

    def test_binary_search_single_element_not_exists(self, solution: Solution) -> None:
        haystack = [42]
        result = solution.binary_search(haystack, 99)
        if result:
            raise ValueError(
                "Should not find non-existent element in single element array",
            )

    def test_binary_search_even_length_exists(self, solution: Solution) -> None:
        haystack = [2, 4, 6, 8, 10, 12]
        result = solution.binary_search(haystack, 8)
        if not result:
            raise ValueError("Should find element in even-length array")

    def test_binary_search_even_length_not_exists(self, solution: Solution) -> None:
        haystack = [2, 4, 6, 8, 10, 12]
        result = solution.binary_search(haystack, 7)
        if result:
            raise ValueError(
                "Should not find non-existent element in even-length array",
            )

    def test_binary_search_odd_length_exists(self, solution: Solution) -> None:
        haystack = [1, 3, 5, 7, 9]
        result = solution.binary_search(haystack, 5)
        if not result:
            raise ValueError("Should find element in odd-length array")

    def test_binary_search_duplicate_values(self, solution: Solution) -> None:
        haystack = [1, 2, 2, 2, 3, 4, 5]
        result = solution.binary_search(haystack, 2)
        if not result:
            raise ValueError(
                "Should find duplicate value (though which duplicate is implementation-dependent)",
            )

    def test_binary_search_negative_numbers(self, solution: Solution) -> None:
        haystack = [-5, -3, -1, 0, 2, 4, 6]
        result = solution.binary_search(haystack, -3)
        if not result:
            raise ValueError("Should find negative number")

    def test_binary_search_large_array(self, solution: Solution) -> None:
        haystack = list(range(1, 1001))  # [1, 2, 3, ..., 1000]
        result = solution.binary_search(haystack, 750)
        if not result:
            raise ValueError("Should find element in large array")

    def test_binary_search_large_array_not_exists(self, solution: Solution) -> None:
        haystack = list(range(1, 1001))  # [1, 2, 3, ..., 1000]
        result = solution.binary_search(haystack, 1500)
        if result:
            raise ValueError("Should not find non-existent element in large array")
