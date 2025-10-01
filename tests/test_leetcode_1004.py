import pytest

from leetcode_1004 import Solution


class TestMaxConsecutiveOnesIII:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_basic_case_flip_two_zeros(self, solution: Solution) -> None:
        """Test basic case with k=2 flips."""
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        expected = 6
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for nums={nums}, k={k}"
            pytest.fail(msg)

    def test_longer_array_with_three_flips(self, solution: Solution) -> None:
        """Test longer array with k=3 flips."""
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        expected = 10
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for longer array with k={k}"
            pytest.fail(msg)

    def test_all_ones_no_flips_needed(self, solution: Solution) -> None:
        """Test array with all ones requires no flips."""
        nums = [1, 1, 1, 1, 1]
        k = 0
        expected = 5
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for all ones array"
            pytest.fail(msg)

    def test_all_zeros_with_sufficient_k(self, solution: Solution) -> None:
        """Test array with all zeros and sufficient k."""
        nums = [0, 0, 0, 0, 0]
        k = 3
        expected = 3
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for all zeros with k={k}"
            pytest.fail(msg)

    def test_k_larger_than_array_length(self, solution: Solution) -> None:
        """Test when k is larger than array length."""
        nums = [0, 1, 0, 1]
        k = 10
        expected = 4
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} when k > array length"
            pytest.fail(msg)

    def test_k_zero_with_zeros_in_array(self, solution: Solution) -> None:
        """Test with k=0 and array containing zeros."""
        nums = [1, 0, 1, 1, 0, 1]
        k = 0
        expected = 2
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} with k=0 and zeros present"
            pytest.fail(msg)

    def test_single_element_zero_with_k_zero(self, solution: Solution) -> None:
        """Test single zero element with k=0."""
        nums = [0]
        k = 0
        expected = 0
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for single zero with k=0"
            pytest.fail(msg)

    def test_single_element_one_with_k_zero(self, solution: Solution) -> None:
        """Test single one element with k=0."""
        nums = [1]
        k = 0
        expected = 1
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for single one with k=0"
            pytest.fail(msg)

    def test_single_element_zero_with_k_one(self, solution: Solution) -> None:
        """Test single zero element with k=1."""
        nums = [0]
        k = 1
        expected = 1
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for single zero with k=1"
            pytest.fail(msg)

    def test_alternating_zeros_ones_with_sufficient_k(self, solution: Solution) -> None:
        """Test alternating pattern with exactly sufficient k."""
        nums = [0, 1, 0, 1, 0, 1, 0]  # 4 zeros total
        k = 3
        # With 3 flips, we can get 6 consecutive ones (leaving 1 zero)
        # Example: flip first 3 zeros → [1,1,1,1,0,1,0] = max 4 consecutive
        # Better: flip middle 3 zeros → [0,1,1,1,1,1,0] = max 5 consecutive
        # Best: flip any 3 zeros strategically to get 6 consecutive
        # [1,1,0,1,1,1,1] if flip positions 0,2,4? Let's check:
        # Original: [0,1,0,1,0,1,0]
        # Flip indices 2,4,6: [0,1,1,1,1,1,1] = 6 consecutive ones
        expected = 6
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = (
                f"Expected {expected}, got {result} for alternating pattern with k={k}"
            )
            pytest.fail(msg)

    def test_maximum_length_constraint(self, solution: Solution) -> None:
        """Test with maximum array length constraint."""
        nums = [1] * 10**5
        k = 0
        expected = 10**5
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = "Failed maximum length array test with all ones"
            pytest.fail(msg)

    def test_zeros_at_beginning_with_sufficient_k(self, solution: Solution) -> None:
        """Test zeros at beginning with sufficient k."""
        nums = [0, 0, 0, 1, 1, 1, 0, 1]
        k = 3
        expected = 7
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for zeros at beginning"
            pytest.fail(msg)

    def test_zeros_at_end_with_sufficient_k(self, solution: Solution) -> None:
        """Test zeros at end with sufficient k."""
        nums = [1, 1, 1, 0, 0, 0]
        k = 3
        expected = 6
        result = solution.function_under_test(nums, k)
        if result != expected:
            msg = f"Expected {expected}, got {result} for zeros at end"
            pytest.fail(msg)
