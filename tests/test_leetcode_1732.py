import pytest

from leetcode_1732 import Solution


class TestHighestAltitude:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test case from example 1."""
        gain = [-5, 1, 5, 0, -7]
        expected = 1
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_example_2(self, solution: Solution) -> None:
        """Test case from example 2."""
        gain = [-4, -3, -2, -1, 4, 3, 2]
        expected = 0
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_single_positive_gain(self, solution: Solution) -> None:
        """Test with single positive gain value."""
        gain = [10]
        expected = 10
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_single_negative_gain(self, solution: Solution) -> None:
        """Test with single negative gain value."""
        gain = [-5]
        expected = 0
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_all_negative_gains(self, solution: Solution) -> None:
        """Test when all gains are negative."""
        gain = [-1, -2, -3, -4, -5]
        expected = 0
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_all_positive_gains(self, solution: Solution) -> None:
        """Test when all gains are positive."""
        gain = [1, 2, 3, 4, 5]
        expected = 15
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_mixed_gains_max_at_end(self, solution: Solution) -> None:
        """Test mixed gains with maximum altitude at the end."""
        gain = [1, -1, 2, -1, 3, -1, 4]
        expected = 7
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_mixed_gains_max_in_middle(self, solution: Solution) -> None:
        """Test mixed gains with maximum altitude in the middle."""
        gain = [2, 3, -10, 1, 1]
        expected = 5
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_zero_gains(self, solution: Solution) -> None:
        """Test when all gains are zero."""
        gain = [0, 0, 0, 0, 0]
        expected = 0
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_minimum_constraints(self, solution: Solution) -> None:
        """Test with minimum array length constraint."""
        gain = [1]
        expected = 1
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain {gain}"
            pytest.fail(error_msg)

    def test_maximum_constraints(self, solution: Solution) -> None:
        """Test with maximum array length constraint."""
        gain = [1] * 100
        expected = 100
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for array length 100"
            pytest.fail(error_msg)

    def test_minimum_gain_value(self, solution: Solution) -> None:
        """Test with minimum gain value constraint."""
        gain = [-100]
        expected = 0
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain -100"
            pytest.fail(error_msg)

    def test_maximum_gain_value(self, solution: Solution) -> None:
        """Test with maximum gain value constraint."""
        gain = [100]
        expected = 100
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for gain 100"
            pytest.fail(error_msg)

    def test_alternating_gains(self, solution: Solution) -> None:
        """Test with alternating positive and negative gains."""
        gain = [5, -3, 4, -2, 3, -1]
        expected = 7  # Corrected from 6 to 7
        result = solution.function_under_test(gain)

        if result != expected:
            error_msg = f"Expected {expected}, got {result} for alternating gains"
            pytest.fail(error_msg)
