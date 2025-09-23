import pytest

from leetcode_0443 import Solution


class TestStringCompression:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_single_character_returns_unchanged(self, solution: Solution) -> None:
        """Test that a single character array returns length 1 unchanged."""
        chars: list[str] = ["a"]
        expected_chars: list[str] = ["a"]
        expected_length: int = 1

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_consecutive_duplicates_are_compressed(self, solution: Solution) -> None:
        """Test that consecutive duplicate characters are properly compressed."""
        chars: list[str] = ["a", "a", "b", "b", "c", "c", "c"]
        expected_chars: list[str] = ["a", "2", "b", "2", "c", "3"]
        expected_length: int = 6

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_long_group_length_splits_into_multiple_digits(
        self,
        solution: Solution,
    ) -> None:
        """Test that group lengths 10 or greater are split into multiple digits."""
        chars: list[str] = [
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
        ]
        expected_chars: list[str] = ["a", "b", "1", "2"]
        expected_length: int = 4

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_mixed_characters_with_various_lengths(self, solution: Solution) -> None:
        """Test compression with mixed characters and varying group lengths."""
        chars: list[str] = ["a", "a", "a", "b", "c", "c", "d", "d", "d", "d"]
        expected_chars: list[str] = ["a", "3", "b", "c", "2", "d", "4"]
        expected_length: int = 7

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_all_single_characters_remain_unchanged(self, solution: Solution) -> None:
        """Test that arrays with all single characters remain uncompressed."""
        chars: list[str] = ["a", "b", "c", "d", "e"]
        expected_chars: list[str] = ["a", "b", "c", "d", "e"]
        expected_length: int = 5

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_maximum_constraint_length(self, solution: Solution) -> None:
        """Test with maximum constraint length of 2000 characters."""
        chars: list[str] = ["x"] * 2000
        expected_chars: list[str] = ["x", "2", "0", "0", "0"]
        expected_length: int = 5

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_digits_and_symbols_are_handled_correctly(self, solution: Solution) -> None:
        """Test that digits and symbols are properly compressed."""
        chars: list[str] = ["1", "1", "#", "#", "#", "$"]
        expected_chars: list[str] = ["1", "2", "#", "3", "$"]
        expected_length: int = 5

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_uppercase_and_lowercase_are_treated_differently(
        self,
        solution: Solution,
    ) -> None:
        """Test that uppercase and lowercase letters are treated as different characters."""
        chars: list[str] = ["a", "A", "A", "b", "B", "B", "B"]
        expected_chars: list[str] = ["a", "A", "2", "b", "B", "3"]
        expected_length: int = 6

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_single_group_at_end_with_length_greater_than_9(
        self,
        solution: Solution,
    ) -> None:
        """Test a single group at the end with length greater than 9."""
        chars: list[str] = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected_chars: list[str] = ["a", "b", "1", "1"]
        expected_length: int = 4

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)

    def test_empty_array_handling(self, solution: Solution) -> None:
        """Test that minimum length constraint of 1 is handled."""
        chars: list[str] = ["z"]
        expected_chars: list[str] = ["z"]
        expected_length: int = 1

        result_length: int = solution.function_under_test(chars)

        if result_length != expected_length:
            message: str = f"Expected length {expected_length}, got {result_length}"
            pytest.fail(message)

        if chars[:result_length] != expected_chars:
            message = f"Expected chars {expected_chars}, got {chars[:result_length]}"
            pytest.fail(message)
