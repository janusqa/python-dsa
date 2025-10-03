import pytest

from leetcode_1493 import Solution


class TestLongestSubarrayOfOnes:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test case with basic deletion scenario."""
        nums = [1, 1, 0, 1]
        result = solution.function_under_test(nums)
        expected = 3

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_example_2(self, solution: Solution) -> None:
        """Test case with multiple zeros and optimal deletion."""
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        result = solution.function_under_test(nums)
        expected = 5

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_example_3(self, solution: Solution) -> None:
        """Test case where all elements are ones."""
        nums = [1, 1, 1]
        result = solution.function_under_test(nums)
        expected = 2

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_all_zeros(self, solution: Solution) -> None:
        """Test case where array contains only zeros."""
        nums = [0, 0, 0, 0]
        result = solution.function_under_test(nums)
        expected = 0

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_single_one(self, solution: Solution) -> None:
        """Test case with only one one in the array."""
        nums = [0, 0, 1, 0]
        result = solution.function_under_test(nums)
        expected = 1

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_single_zero(self, solution: Solution) -> None:
        """Test case with only one zero in the array."""
        nums = [1, 1, 0, 1, 1]
        result = solution.function_under_test(nums)
        expected = 4

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_consecutive_zeros(self, solution: Solution) -> None:
        """Test case with multiple consecutive zeros."""
        nums = [1, 0, 0, 1, 1, 1]
        result = solution.function_under_test(nums)
        expected = 3

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_empty_after_deletion(self, solution: Solution) -> None:
        """Test case where deletion leaves no elements."""
        nums = [0]
        result = solution.function_under_test(nums)
        expected = 0

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_large_input(self, solution: Solution) -> None:
        """Test case with maximum constraint size."""
        nums = [1] * 10**5
        result = solution.function_under_test(nums)
        expected = 10**5 - 1

        if result != expected:
            msg = f"Expected {expected} but got {result} for large input"
            pytest.fail(msg)

    def test_alternating_ones_zeros(self, solution: Solution) -> None:
        """Test case with alternating pattern of ones and zeros."""
        nums = [1, 0, 1, 0, 1, 0, 1]
        result = solution.function_under_test(nums)
        expected = 2

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_deletion_at_beginning(self, solution: Solution) -> None:
        """Test case where optimal deletion is at the beginning."""
        nums = [0, 1, 1, 1, 1]
        result = solution.function_under_test(nums)
        expected = 4

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)

    def test_deletion_at_end(self, solution: Solution) -> None:
        """Test case where optimal deletion is at the end."""
        nums = [1, 1, 1, 1, 0]
        result = solution.function_under_test(nums)
        expected = 4

        if result != expected:
            msg = f"Expected {expected} but got {result} for input {nums}"
            pytest.fail(msg)
            pytest.fail(msg)
