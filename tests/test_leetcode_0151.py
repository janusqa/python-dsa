import pytest

from leetcode_0151 import Solution


class TestReverseWords:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1_basic_reversal(self, solution: Solution) -> None:
        """Test basic word reversal with single spaces."""
        input_str = "the sky is blue"
        result = solution.reverse_words(input_str)
        expected = "blue is sky the"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_example_2_leading_trailing_spaces(self, solution: Solution) -> None:
        """Test string with leading and trailing spaces."""
        input_str = "  hello world  "
        result = solution.reverse_words(input_str)
        expected = "world hello"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_example_3_multiple_internal_spaces(self, solution: Solution) -> None:
        """Test string with multiple internal spaces between words."""
        input_str = "a good   example"
        result = solution.reverse_words(input_str)
        expected = "example good a"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_single_word(self, solution: Solution) -> None:
        """Test string with only one word."""
        input_str = "hello"
        result = solution.reverse_words(input_str)
        expected = "hello"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_all_spaces(self, solution: Solution) -> None:
        """Test string containing only spaces."""
        input_str = "     "
        result = solution.reverse_words(input_str)
        expected = ""
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_mixed_case_words(self, solution: Solution) -> None:
        """Test words with mixed uppercase and lowercase letters."""
        input_str = "Hello World From Python"
        result = solution.reverse_words(input_str)
        expected = "Python From World Hello"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_words_with_numbers(self, solution: Solution) -> None:
        """Test string containing words with numbers."""
        input_str = "123 abc 456 def"
        result = solution.reverse_words(input_str)
        expected = "def 456 abc 123"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_maximum_length_string(self, solution: Solution) -> None:
        """Test with maximum length string near constraint limit."""
        max_length = 10**4
        words = ["word"] * (max_length // 5)
        input_str = " ".join(words)

        if len(input_str) > max_length:
            input_str = input_str[:max_length]

        result = solution.reverse_words(input_str)

        if len(result) > max_length:
            error_msg = (
                f"Result length {len(result)} exceeds maximum constraint {max_length}"
            )
            pytest.fail(error_msg)

    def test_minimum_length_string(self, solution: Solution) -> None:
        """Test with minimum length string."""
        input_str = "a"
        result = solution.reverse_words(input_str)
        expected = "a"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_multiple_spaces_between_every_word(self, solution: Solution) -> None:
        """Test string with multiple spaces between every word."""
        input_str = "a  b  c  d  e"
        result = solution.reverse_words(input_str)
        expected = "e d c b a"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_string_with_leading_trailing_and_internal_spaces(
        self,
        solution: Solution,
    ) -> None:
        """Test string with all types of extra spaces."""
        input_str = "   this   is    a   test   "
        result = solution.reverse_words(input_str)
        expected = "test a is this"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_english_letters_upper_lower_case(self, solution: Solution) -> None:
        """Test with English letters in various cases."""
        input_str = "Apple Banana Cherry Date"
        result = solution.reverse_words(input_str)
        expected = "Date Cherry Banana Apple"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_digits_as_words(self, solution: Solution) -> None:
        """Test with digits treated as individual words."""
        input_str = "1 22 333 4444"
        result = solution.reverse_words(input_str)
        expected = "4444 333 22 1"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_mixed_alphanumeric_words(self, solution: Solution) -> None:
        """Test with words containing both letters and numbers."""
        input_str = "test123 code456 python789"
        result = solution.reverse_words(input_str)
        expected = "python789 code456 test123"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_no_extra_spaces_in_result(self, solution: Solution) -> None:
        """Test that result contains no leading, trailing, or multiple spaces."""
        input_str = "   multiple   spaces   here   "
        result = solution.reverse_words(input_str)

        if result.startswith(" ") or result.endswith(" "):
            error_msg = f"Result contains leading or trailing spaces: '{result}'"
            pytest.fail(error_msg)

        if "  " in result:
            error_msg = f"Result contains multiple consecutive spaces: '{result}'"
            pytest.fail(error_msg)

    def test_large_number_of_small_words(self, solution: Solution) -> None:
        """Test with a large number of single-character words."""
        input_str = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        result = solution.reverse_words(input_str)
        expected = "z y x w v u t s r q p o n m l k j i h g f e d c b a"
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)

    def test_string_with_only_one_space(self, solution: Solution) -> None:
        """Test string containing only a single space."""
        input_str = " "
        result = solution.reverse_words(input_str)
        expected = ""
        if result != expected:
            error_msg = f"Expected '{expected}', got '{result}'"
            pytest.fail(error_msg)
