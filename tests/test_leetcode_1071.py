import pytest

from leetcode_1071 import Solution  # Replace with your actual module name


class TestGCDOfStrings:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_example_1(self, solution: Solution) -> None:
        """Test example 1 from the problem description."""
        str1 = "ABCABC"
        str2 = "ABC"
        result = solution.gcd_of_strings(str1, str2)
        if result != "ABC":
            raise AssertionError("Expected 'ABC' for str1='ABCABC' and str2='ABC'")

    def test_example_2(self, solution: Solution) -> None:
        """Test example 2 from the problem description."""
        str1 = "ABABAB"
        str2 = "ABAB"
        result = solution.gcd_of_strings(str1, str2)
        if result != "AB":
            raise AssertionError("Expected 'AB' for str1='ABABAB' and str2='ABAB'")

    def test_example_3(self, solution: Solution) -> None:
        """Test example 3 from the problem description."""
        str1 = "LEET"
        str2 = "CODE"
        result = solution.gcd_of_strings(str1, str2)
        if result != "":
            raise AssertionError(
                "Expected empty string for str1='LEET' and str2='CODE'",
            )

    def test_identical_strings(self, solution: Solution) -> None:
        """Test with identical strings."""
        str1 = "TESTTEST"
        str2 = "TESTTEST"
        result = solution.gcd_of_strings(str1, str2)
        if result != "TESTTEST":
            raise AssertionError("Expected full string for identical strings")

    def test_one_string_empty(self, solution: Solution) -> None:
        """Test when one string is empty."""
        str1 = ""
        str2 = "ABC"
        result = solution.gcd_of_strings(str1, str2)
        if result != "":
            raise AssertionError("Expected empty string when one input is empty")

    def test_both_strings_empty(self, solution: Solution) -> None:
        """Test when both strings are empty."""
        str1 = ""
        str2 = ""
        result = solution.gcd_of_strings(str1, str2)
        if result != "":
            raise AssertionError("Expected empty string when both inputs are empty")

    def test_largest_possible_divisor(self, solution: Solution) -> None:
        """Test that returns largest possible divisor, not just any divisor."""
        str1 = "AAAAAA"  # 6 characters
        str2 = "AAA"  # 3 characters
        result = solution.gcd_of_strings(str1, str2)
        # GCD(6, 3) = 3, so should return "AAA" (largest), not "A"
        if result != "AAA":
            raise AssertionError(
                "Expected 'AAA' (largest divisor) for str1='AAAAAA' and str2='AAA'",
            )

    def test_multi_character_largest_divisor(self, solution: Solution) -> None:
        """Test multi-character largest divisor."""
        str1 = "ABABABAB"  # 8 characters
        str2 = "ABAB"  # 4 characters
        result = solution.gcd_of_strings(str1, str2)
        # GCD(8, 4) = 4, so should return "ABAB" (largest), not "AB"
        if result != "ABAB":
            raise AssertionError(
                "Expected 'ABAB' (largest divisor) for str1='ABABABAB' and str2='ABAB'",
            )

    def test_no_common_divisor(self, solution: Solution) -> None:
        """Test case where no common divisor exists."""
        str1 = "ABCDEF"
        str2 = "XYZ"
        result = solution.gcd_of_strings(str1, str2)
        if result != "":
            raise AssertionError(
                "Expected empty string for strings with no common divisor",
            )

    def test_different_lengths_same_pattern(self, solution: Solution) -> None:
        """Test strings with same pattern but different lengths."""
        str1 = "ABCABCABC"  # 9 characters
        str2 = "ABC"  # 3 characters
        result = solution.gcd_of_strings(str1, str2)
        # GCD(9, 3) = 3, so should return "ABC" (largest)
        if result != "ABC":
            raise AssertionError("Expected 'ABC' for same pattern different lengths")

    def test_partial_but_not_full_divisor(self, solution: Solution) -> None:
        """Test case where smaller string doesn't fully divide larger string."""
        str1 = "ABCDABCDABCD"  # 12 characters
        str2 = "ABCDAB"  # 6 characters
        result = solution.gcd_of_strings(str1, str2)
        # No common divisor since "ABCDAB" doesn't divide "ABCDABCDABCD"
        if result != "":
            raise AssertionError("Expected empty string when no common divisor exists")

    def test_largest_common_divisor_complex(self, solution: Solution) -> None:
        """Test complex case for largest common divisor."""
        str1 = "XYZXYZXYZXYZ"  # 12 characters (4 repetitions of "XYZ")
        str2 = "XYZXYZ"  # 6 characters (2 repetitions of "XYZ")
        result = solution.gcd_of_strings(str1, str2)
        # GCD(12, 6) = 6, so should return "XYZXYZ" (largest), not "XYZ"
        if result != "XYZXYZ":
            raise AssertionError("Expected 'XYZXYZ' (largest divisor) not 'XYZ'")
