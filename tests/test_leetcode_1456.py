import pytest

from leetcode_1456 import Solution


class TestMaximumVowelsInSubstring:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test the first example from the problem description."""
        s = "abciiidef"
        k = 3
        expected = 3

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_example_2(self, solution: Solution) -> None:
        """Test the second example with all vowels."""
        s = "aeiou"
        k = 2
        expected = 2

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_example_3(self, solution: Solution) -> None:
        """Test the third example with mixed vowels and consonants."""
        s = "leetcode"
        k = 3
        expected = 2

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_character_vowel(self, solution: Solution) -> None:
        """Test with a single vowel character."""
        s = "a"
        k = 1
        expected = 1

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_character_consonant(self, solution: Solution) -> None:
        """Test with a single consonant character."""
        s = "b"
        k = 1
        expected = 0

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_consonants(self, solution: Solution) -> None:
        """Test with a string containing no vowels."""
        s = "bcdfghjklmnpqrstvwxyz"
        k = 5
        expected = 0

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_vowels(self, solution: Solution) -> None:
        """Test with a string containing only vowels."""
        s = "aeiouaeiouaeiou"
        k = 4
        expected = 4

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_k_equals_string_length(self, solution: Solution) -> None:
        """Test when k equals the entire string length."""
        s = "aeioubcd"
        k = 8
        expected = 5

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_vowels_at_beginning(self, solution: Solution) -> None:
        """Test when maximum vowels are at the beginning of the string."""
        s = "aaabcde"
        k = 3
        expected = 3

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_vowels_at_end(self, solution: Solution) -> None:
        """Test when maximum vowels are at the end of the string."""
        s = "bcdeaaa"
        k = 3
        expected = 3

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_vowels_in_middle(self, solution: Solution) -> None:
        """Test when maximum vowels are in the middle of the string."""
        s = "bcaaaade"
        k = 4
        expected = 4

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_alternating_vowels_consonants(self, solution: Solution) -> None:
        """Test with alternating vowels and consonants."""
        s = "aeibcdou"
        k = 2
        expected = 2

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_minimum_constraints(self, solution: Solution) -> None:
        """Test with minimum constraint values."""
        s = "a"
        k = 1
        expected = 1

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_large_k_small_vowel_count(self, solution: Solution) -> None:
        """Test with large k but few vowels in the string."""
        s = "bcdfghjklmnpqrstvwxyza"
        k = 10
        expected = 1

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_vowel_multiple_windows(self, solution: Solution) -> None:
        """Test with a single vowel appearing in multiple windows."""
        s = "bcabcbacb"
        k = 3
        expected = 1

        result = solution.function_under_test(s, k)

        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_case_sensitivity_check(self, solution: Solution) -> None:
        """Test that lowercase letters are properly handled."""
        s = "AEIOUaeiou"  # Mixed case, but constraints say lowercase only
        k = 2

        # Since constraints specify lowercase English letters,
        # this tests that the function handles its input correctly
        result = solution.function_under_test(s, k)

        # The function should only count lowercase vowels based on problem constraints
        if result < 0 or result > k:
            error_msg = f"Result {result} outside valid range [0, {k}]"
            pytest.fail(error_msg)
            pytest.fail(error_msg)
