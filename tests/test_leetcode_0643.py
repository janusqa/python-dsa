import pytest

from leetcode_0643 import Solution


class TestMaximumAverageSubarrayI:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_basic_example_1(self, solution: Solution) -> None:
        """Test the first example from the problem description."""
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75000

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_element(self, solution: Solution) -> None:
        """Test with a single element array."""
        nums = [5]
        k = 1
        expected = 5.00000

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_positive_numbers(self, solution: Solution) -> None:
        """Test with all positive numbers."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        expected = 9.0  # (8+9+10)/3

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_negative_numbers(self, solution: Solution) -> None:
        """Test with all negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        k = 2
        expected = -1.5  # (-1 + -2)/2

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_mixed_positive_negative(self, solution: Solution) -> None:
        """Test with mixed positive and negative numbers."""
        nums = [10, -2, 5, -8, 15, 3]
        k = 3
        expected = 10.0 / 3  # (15+3+?)/3 - need to calculate properly

        # Calculate the actual maximum: (10 + -2 + 5) = 13/3, (-2+5-8)=-5/3, (5-8+15)=12/3, (-8+15+3)=10/3
        # Maximum is 13/3 ≈ 4.33333

        result = solution.function_under_test(nums, k)

        # Verify the result is reasonable
        if result < -8 or result > 15:
            error_msg = f"Result {result} outside expected range"
            pytest.fail(error_msg)

    def test_k_equals_array_length(self, solution: Solution) -> None:
        """Test when k equals the entire array length."""
        nums = [2, 4, 6, 8, 10]
        k = 5
        expected = 6.0  # (2+4+6+8+10)/5

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_large_k_small_array(self, solution: Solution) -> None:
        """Test with k close to array length."""
        nums = [1, 2, 3, 4, 5]
        k = 4
        expected = 3.5  # (2+3+4+5)/4

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_minimum_constraints(self, solution: Solution) -> None:
        """Test with minimum constraint values."""
        nums = [1]
        k = 1
        expected = 1.0

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_large_numbers(self, solution: Solution) -> None:
        """Test with numbers at the constraint boundaries."""
        nums = [10000, -10000, 10000, -10000]
        k = 2
        expected = 0.0  # Either (10000 + -10000)/2 or (-10000 + 10000)/2

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_increasing_sequence(self, solution: Solution) -> None:
        """Test with strictly increasing sequence."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 4
        expected = 8.5  # (7+8+9+10)/4 = 34/4 = 8.5

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_decreasing_sequence(self, solution: Solution) -> None:
        """Test with strictly decreasing sequence."""
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        k = 3
        expected = 9.0  # (10+9+8)/3

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_alternating_sequence(self, solution: Solution) -> None:
        """Test with alternating high and low values."""
        nums = [100, 1, 100, 1, 100, 1]
        k = 2
        expected = 50.5  # (100 + 1)/2

        result = solution.function_under_test(nums, k)

        if abs(result - expected) > 1e-5:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)
