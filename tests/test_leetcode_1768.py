import sys
from pathlib import Path

import pytest

# Add the parent directory to Python path so we can import myapp
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from src.leetcode_1786 import Solution


class TestLeetcode1786:
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()

    def _assert_equal(self, actual: str, expected: str, context: str = "") -> None:
        """Helper function to compare values with clean error messages."""
        if actual != expected:
            error_msg = f"{context}Expected '{expected}', got '{actual}'"
            raise ValueError(error_msg)

    def test_merge_alternately_equal_length(self, solution: Solution) -> None:
        result = solution.merge_alternately("abc", "pqr")
        self._assert_equal(result, "apbqcr", "Equal length words: ")

        result = solution.merge_alternately("ab", "pq")
        self._assert_equal(result, "apbq", "Equal length words: ")

        result = solution.merge_alternately("a", "p")
        self._assert_equal(result, "ap", "Single character words: ")

    def test_merge_alternately_first_word_longer(self, solution: Solution) -> None:
        result = solution.merge_alternately("abcd", "pq")
        self._assert_equal(result, "apbqcd", "First word longer: ")

        result = solution.merge_alternately("abc", "p")
        self._assert_equal(result, "apbc", "First word longer: ")

        result = solution.merge_alternately("abcdef", "xyz")
        self._assert_equal(result, "axbyczdef", "First word longer: ")

    def test_merge_alternately_second_word_longer(self, solution: Solution) -> None:
        result = solution.merge_alternately("ab", "pqrs")
        self._assert_equal(result, "apbqrs", "Second word longer: ")

        result = solution.merge_alternately("a", "pqr")
        self._assert_equal(result, "apqr", "Second word longer: ")

        result = solution.merge_alternately("xy", "abcdef")
        self._assert_equal(result, "xaybcdef", "Second word longer: ")

    def test_merge_alternately_edge_cases(self, solution: Solution) -> None:
        result = solution.merge_alternately("", "")
        self._assert_equal(result, "", "Both empty strings: ")

        result = solution.merge_alternately("abc", "")
        self._assert_equal(result, "abc", "Second string empty: ")

        result = solution.merge_alternately("", "xyz")
        self._assert_equal(result, "xyz", "First string empty: ")

        result = solution.merge_alternately("a", "b")
        self._assert_equal(result, "ab", "Single characters: ")

    def test_merge_alternately_long_words(self, solution: Solution) -> None:
        result = solution.merge_alternately("abcdefgh", "ijklmnop")
        expected = "aibjckdlemfngohp"
        self._assert_equal(result, expected, "Long words: ")
