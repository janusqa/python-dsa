import pytest

from leetcode_0238 import Solution


class TestProductOfArrayExceptSelf:
    """Test class for product of array except self functionality."""

    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example1(self, solution: Solution) -> None:
        """Test the function with example input [1,2,3,4]."""
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_example2(self, solution: Solution) -> None:
        """Test the function with example input [-1,1,0,-3,3]."""
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_negative_numbers(self, solution: Solution) -> None:
        """Test the function with negative numbers."""
        nums = [-2, -3, -4]
        expected = [12, 8, 6]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_minimum_length(self, solution: Solution) -> None:
        """Test the function with minimum array length of 2."""
        nums = [5, 10]
        expected = [10, 5]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_multiple_zeros(self, solution: Solution) -> None:
        """Test the function with multiple zeros in array."""
        nums = [0, 0, 2, 3]
        expected = [0, 0, 0, 0]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_large_array(self, solution: Solution) -> None:
        """Test the function with a large array."""
        nums = [1] * 1000
        expected = [1] * 1000
        result = solution.function_under_test(nums)
        error_message = "Large array test failed"
        if result != expected:
            pytest.fail(error_message)

    def test_all_same_elements(self, solution: Solution) -> None:
        """Test the function with all elements being the same."""
        nums = [3, 3, 3, 3]
        expected = [27, 27, 27, 27]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)

    def test_mixed_positive_negative(self, solution: Solution) -> None:
        """Test the function with mixed positive and negative numbers."""
        nums = [2, -1, 3, -4]
        expected = [12, -24, 8, -6]
        result = solution.function_under_test(nums)
        error_message = f"Expected {expected}, but got {result}"
        if result != expected:
            pytest.fail(error_message)
            pytest.fail(error_message)
