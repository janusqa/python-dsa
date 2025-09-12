import sys
from pathlib import Path

import pytest

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from bubble_sort import Solution  # Assuming your class is in myapp.py


class TestBubbleSort:
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()

    def test_bubble_sort_normal_case(self, solution: Solution) -> None:
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Normal case failed: Expected " + str(expected) + ", got " + str(arr),
            )

    def test_bubble_sort_already_sorted(self, solution: Solution) -> None:
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Already sorted case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_reverse_sorted(self, solution: Solution) -> None:
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Reverse sorted case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_duplicate_values(self, solution: Solution) -> None:
        arr = [5, 2, 8, 2, 5, 8, 1]
        expected = [1, 2, 2, 5, 5, 8, 8]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Duplicate values case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_single_element(self, solution: Solution) -> None:
        arr = [42]
        expected = [42]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Single element case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_empty_list(self, solution: Solution) -> None:
        arr: list[int] = []
        expected: list[int] = []
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Empty list case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_negative_numbers(self, solution: Solution) -> None:
        arr = [-5, -1, -8, 0, 3, -2]
        expected = [-8, -5, -2, -1, 0, 3]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Negative numbers case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_two_elements(self, solution: Solution) -> None:
        arr = [3, 1]
        expected = [1, 3]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Two elements case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

        arr = [1, 3]
        expected = [1, 3]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Two elements (already sorted) case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )

    def test_bubble_sort_identical_elements(self, solution: Solution) -> None:
        arr = [7, 7, 7, 7]
        expected = [7, 7, 7, 7]
        solution.bubble_sort(arr)
        if arr != expected:
            raise ValueError(
                "Identical elements case failed: Expected "
                + str(expected)
                + ", got "
                + str(arr),
            )
