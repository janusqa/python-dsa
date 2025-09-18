import pytest

from leetcode_0345 import Solution


class TestReverseVowels:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1_mixed_case_vowels(self, solution: Solution) -> None:
        """Test example 1 with mixed case vowels."""
        s = "IceCreAm"
        result = solution.reverse_vowels(s)
        expected = "AceCreIm"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_example_2_all_lowercase(self, solution: Solution) -> None:
        """Test example 2 with all lowercase."""
        s = "leetcode"
        result = solution.reverse_vowels(s)
        expected = "leotcede"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_two_vowels_with_different_cases(self, solution: Solution) -> None:
        """Test two vowels with different cases."""
        s = "aA"
        result = solution.reverse_vowels(s)
        expected = "Aa"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_string_with_no_vowels(self, solution: Solution) -> None:
        """Test string with no vowels."""
        s = "bcdfg"
        result = solution.reverse_vowels(s)
        expected = "bcdfg"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_vowel(self, solution: Solution) -> None:
        """Test single vowel."""
        s = "a"
        result = solution.reverse_vowels(s)
        expected = "a"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_single_consonant(self, solution: Solution) -> None:
        """Test single consonant."""
        s = "b"
        result = solution.reverse_vowels(s)
        expected = "b"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_vowels_in_order(self, solution: Solution) -> None:
        """Test all vowels in order."""
        s = "aeiou"
        result = solution.reverse_vowels(s)
        expected = "uoiea"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_uppercase_vowels(self, solution: Solution) -> None:
        """Test all uppercase vowels."""
        s = "AEIOU"
        result = solution.reverse_vowels(s)
        expected = "UOIEA"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_empty_string(self, solution: Solution) -> None:
        """Test empty string."""
        s = ""
        result = solution.reverse_vowels(s)
        expected = ""
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_vowels_with_spaces(self, solution: Solution) -> None:
        """Test vowels with spaces."""
        s = "a e i o u"
        result = solution.reverse_vowels(s)
        expected = "u o i e a"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_string_with_punctuation(self, solution: Solution) -> None:
        """Test string with punctuation."""
        s = "Hello World!"
        result = solution.reverse_vowels(s)
        expected = "Hollo Werld!"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_large_string_near_constraint_limit(self, solution: Solution) -> None:
        """Test with large string near constraint limit."""
        max_length = 3 * 10**5
        large_string = "aB" * (max_length // 2)
        if len(large_string) < max_length:
            large_string += "a"

        result = solution.reverse_vowels(large_string)

        if len(result) != len(large_string):
            error_msg = f"Expected length {len(large_string)}, got {len(result)}"
            pytest.fail(error_msg)

    def test_all_consonants_large_string(self, solution: Solution) -> None:
        """Test large string with all consonants."""
        large_string = "b" * 1000
        result = solution.reverse_vowels(large_string)
        expected = large_string
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_all_vowels_large_string(self, solution: Solution) -> None:
        """Test large string with all vowels."""
        large_string = "aeiou" * 200
        result = solution.reverse_vowels(large_string)
        expected = "uoiea" * 200
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_string_with_numbers_and_special_chars(self, solution: Solution) -> None:
        """Test string with numbers and special characters."""
        s = "H3ll0 W0rld! @#%"
        result = solution.reverse_vowels(s)
        expected = "H3ll0 W0rld! @#%"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_string_with_only_vowels_and_special_chars(
        self,
        solution: Solution,
    ) -> None:
        """Test string with only vowels and special characters."""
        s = "a!e@i#o$u%"
        result = solution.reverse_vowels(s)
        expected = "u!o@i#e$a%"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_consecutive_vowels(self, solution: Solution) -> None:
        """Test string with consecutive vowels."""
        s = "beautiful"
        result = solution.reverse_vowels(s)
        expected = "buiutafel"  # This is the correct expectation
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_vowels_at_beginning_and_end(self, solution: Solution) -> None:
        """Test string with vowels at beginning and end."""
        s = "apple"
        result = solution.reverse_vowels(s)
        expected = "eppla"
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)
