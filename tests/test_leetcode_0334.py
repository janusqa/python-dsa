import pytest

from leetcode_0334 import Solution


class TestIncreasingTripletSubsequence:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_simple_increasing_sequence_returns_true(self, solution: Solution) -> None:
        """Test that a simple increasing sequence returns true."""
        nums: list[int] = [1, 2, 3, 4, 5]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for increasing sequence {nums}"
            pytest.fail(message)

    def test_decreasing_sequence_returns_false(self, solution: Solution) -> None:
        """Test that a strictly decreasing sequence returns false."""
        nums: list[int] = [5, 4, 3, 2, 1]
        result: bool = solution.function_under_test(nums)
        if result:
            message: str = f"Expected False for decreasing sequence {nums}"
            pytest.fail(message)

    def test_valid_triplet_not_at_start_returns_true(self, solution: Solution) -> None:
        """Test that a valid triplet not at sequence start returns true."""
        nums: list[int] = [2, 1, 5, 0, 4, 6]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for sequence with valid triplet {nums}"
            pytest.fail(message)

    def test_minimum_length_array_returns_false(self, solution: Solution) -> None:
        """Test that array with less than 3 elements returns false."""
        nums: list[int] = [1, 2]
        result: bool = solution.function_under_test(nums)
        if result:
            message: str = f"Expected False for short sequence {nums}"
            pytest.fail(message)

    def test_exactly_three_elements_valid_returns_true(
        self,
        solution: Solution,
    ) -> None:
        """Test that exactly three elements with valid triplet returns true."""
        nums: list[int] = [1, 2, 3]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for valid three-element sequence {nums}"
            pytest.fail(message)

    def test_exactly_three_elements_invalid_returns_false(
        self,
        solution: Solution,
    ) -> None:
        """Test that exactly three elements with invalid triplet returns false."""
        nums: list[int] = [3, 2, 1]
        result: bool = solution.function_under_test(nums)
        if result:
            message: str = f"Expected False for invalid three-element sequence {nums}"
            pytest.fail(message)

    def test_duplicate_values_returns_false(self, solution: Solution) -> None:
        """Test that sequences with duplicates but no valid triplet return false."""
        nums: list[int] = [1, 1, 1, 1, 1]
        result: bool = solution.function_under_test(nums)
        if result:
            message: str = f"Expected False for sequence with duplicates {nums}"
            pytest.fail(message)

    def test_large_numbers_valid_triplet_returns_true(self, solution: Solution) -> None:
        """Test that large numbers with valid triplet return true."""
        nums: list[int] = [-(2**31), 0, 2**31 - 1]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = "Expected True for sequence with large number range"
            pytest.fail(message)

    def test_maximum_length_array_valid_returns_true(self, solution: Solution) -> None:
        """Test that maximum length array with valid triplet returns true."""
        nums: list[int] = list(range(500000))
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = "Expected True for maximum length valid sequence"
            pytest.fail(message)

    def test_triplet_at_end_returns_true(self, solution: Solution) -> None:
        """Test that valid triplet at the end of array returns true."""
        nums: list[int] = [5, 4, 3, 1, 2, 3]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for triplet at end {nums}"
            pytest.fail(message)

    def test_multiple_valid_triplets_returns_true(self, solution: Solution) -> None:
        """Test that array with multiple valid triplets returns true."""
        nums: list[int] = [1, 2, 3, 2, 3, 4]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for sequence with multiple triplets {nums}"
            pytest.fail(message)

    def test_strictly_increasing_but_not_consecutive_returns_true(
        self,
        solution: Solution,
    ) -> None:
        """Test that non-consecutive but strictly increasing triplet returns true."""
        nums: list[int] = [1, 3, 2, 4]
        result: bool = solution.function_under_test(nums)
        if not result:
            message: str = f"Expected True for non-consecutive triplet {nums}"
            pytest.fail(message)
            pytest.fail(message)
