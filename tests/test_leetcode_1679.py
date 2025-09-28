import pytest

from leetcode_1679 import Solution


class TestMaxNumberOfKSumPairs:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test basic case with two valid pairs."""
        nums = [1, 2, 3, 4]
        k = 5
        expected = 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_example_2(self, solution: Solution) -> None:
        """Test case with duplicate numbers and one valid pair."""
        nums = [3, 1, 3, 4, 3]
        k = 6
        expected = 1
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_no_pairs_possible(self, solution: Solution) -> None:
        """Test case where no pairs sum to k."""
        nums = [1, 2, 3, 4]
        k = 10
        expected = 0
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_single_element_array(self, solution: Solution) -> None:
        """Test with array containing only one element."""
        nums = [5]
        k = 10
        expected = 0
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_large_numbers_within_constraints(self, solution: Solution) -> None:
        """Test with numbers approaching the upper constraint limit."""
        nums = [10**9, 10**9, 1, 1]
        k = 2
        expected = 1
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_k_at_upper_constraint(self, solution: Solution) -> None:
        """Test with k at the maximum constraint value."""
        nums = [1, 10**9 - 1, 2, 10**9 - 2]
        k = 10**9
        expected = 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_duplicate_pairs(self, solution: Solution) -> None:
        """Test case with multiple identical valid pairs."""
        nums = [2, 2, 2, 2]
        k = 4
        expected = 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_negative_scenario_no_pairs(self, solution: Solution) -> None:
        """Test where numbers cannot form pairs summing to k."""
        nums = [10, 20, 30, 40]
        k = 15
        expected = 0
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_large_array_size(self, solution: Solution) -> None:
        """Test with array size approaching upper constraint."""
        nums = list(range(1, 1001)) * 100  # 100,000 elements
        k = 1001
        expected = 100000 // 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_zero_operations_edge_case(self, solution: Solution) -> None:
        """Test edge case where no operations are possible."""
        nums = [100, 200, 300]
        k = 50
        expected = 0
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_all_elements_form_pairs(self, solution: Solution) -> None:
        """Test case where all elements can form valid pairs."""
        nums = [1, 9, 2, 8, 3, 7]
        k = 10
        expected = 3
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)

    def test_odd_length_array(self, solution: Solution) -> None:
        """Test with odd number of elements where one element remains."""
        nums = [1, 2, 3, 4, 5]
        k = 6
        expected = 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected} operations, got {result}"
            pytest.fail(msg)
