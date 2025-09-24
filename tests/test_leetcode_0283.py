import pytest

from leetcode_0283 import Solution


class TestMoveZeroes:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test the first example case."""
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_example_2(self, solution: Solution) -> None:
        """Test the second example case."""
        nums = [0]
        expected = [0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_all_zeros(self, solution: Solution) -> None:
        """Test an array containing only zeros."""
        nums = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_no_zeros(self, solution: Solution) -> None:
        """Test an array with no zeros."""
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_zeros_at_end(self, solution: Solution) -> None:
        """Test an array where zeros are already at the end."""
        nums = [1, 2, 3, 0, 0]
        expected = [1, 2, 3, 0, 0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_zeros_at_beginning(self, solution: Solution) -> None:
        """Test an array where zeros are at the beginning."""
        nums = [0, 0, 1, 2, 3]
        expected = [1, 2, 3, 0, 0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_mixed_zeros_and_negatives(self, solution: Solution) -> None:
        """Test an array with zeros and negative numbers."""
        nums = [0, -1, 0, 2, -3]
        expected = [-1, 2, -3, 0, 0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_single_element_zero(self, solution: Solution) -> None:
        """Test a single zero element array."""
        nums = [0]
        expected = [0]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_single_element_non_zero(self, solution: Solution) -> None:
        """Test a single non-zero element array."""
        nums = [5]
        expected = [5]
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = f"Expected {expected}, but got {nums}"
            pytest.fail(error_msg)

    def test_large_array(self, solution: Solution) -> None:
        """Test a larger array with mixed zeros and non-zeros."""
        nums = [0] * 50 + [1] * 50
        expected = [1] * 50 + [0] * 50
        solution.function_under_test(nums)
        if nums != expected:
            error_msg = "Large array test failed - order not maintained correctly"
            pytest.fail(error_msg)
            pytest.fail(error_msg)
