import pytest

from leetcode_0392 import Solution


class TestIsSubsequence:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_basic_subsequence_case(self, solution: Solution) -> None:
        """Test basic valid subsequence case."""
        s = "abc"
        t = "ahbgdc"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for s='{s}', t='{t}' but got {result}"
            pytest.fail(msg)

    def test_non_subsequence_case(self, solution: Solution) -> None:
        """Test case where s is not a subsequence of t."""
        s = "axc"
        t = "ahbgdc"
        result = solution.function_under_test(s, t)
        if result:
            msg = f"Expected False for s='{s}', t='{t}' but got {result}"
            pytest.fail(msg)

    def test_empty_s_string(self, solution: Solution) -> None:
        """Test case where s is an empty string."""
        s = ""
        t = "ahbgdc"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for empty s with t='{t}' but got {result}"
            pytest.fail(msg)

    def test_empty_t_string_with_empty_s(self, solution: Solution) -> None:
        """Test case where both s and t are empty strings."""
        s = ""
        t = ""
        result = solution.function_under_test(s, t)
        if not result:
            msg = "Expected True for empty s and empty t but got False"
            pytest.fail(msg)

    def test_empty_t_string_with_non_empty_s(self, solution: Solution) -> None:
        """Test case where t is empty but s is not."""
        s = "abc"
        t = ""
        result = solution.function_under_test(s, t)
        if result:
            msg = f"Expected False for s='{s}' with empty t but got {result}"
            pytest.fail(msg)

    def test_s_longer_than_t(self, solution: Solution) -> None:
        """Test case where s is longer than t."""
        s = "abcdef"
        t = "abc"
        result = solution.function_under_test(s, t)
        if result:
            msg = f"Expected False when len(s) > len(t) but got {result}"
            pytest.fail(msg)

    def test_same_strings(self, solution: Solution) -> None:
        """Test case where s and t are identical."""
        s = "abc"
        t = "abc"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for identical strings but got {result}"
            pytest.fail(msg)

    def test_single_character_match(self, solution: Solution) -> None:
        """Test case with single character match."""
        s = "a"
        t = "abc"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for single character match but got {result}"
            pytest.fail(msg)

    def test_single_character_no_match(self, solution: Solution) -> None:
        """Test case with single character no match."""
        s = "z"
        t = "abc"
        result = solution.function_under_test(s, t)
        if result:
            msg = f"Expected False for single character no match but got {result}"
            pytest.fail(msg)

    def test_characters_in_wrong_order(self, solution: Solution) -> None:
        """Test case where s characters appear in t but in wrong order."""
        s = "ba"
        t = "abc"
        result = solution.function_under_test(s, t)
        if result:
            msg = f"Expected False for wrong character order but got {result}"
            pytest.fail(msg)

    def test_duplicate_characters_in_s(self, solution: Solution) -> None:
        """Test case with duplicate characters in s."""
        s = "aabb"
        t = "ababab"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for duplicate characters but got {result}"
            pytest.fail(msg)

    def test_maximum_constraint_s(self, solution: Solution) -> None:
        """Test case with maximum length s."""
        s = "a" * 100
        t = "a" * 100 + "b" * 4
        result = solution.function_under_test(s, t)
        if not result:
            msg = "Expected True for maximum length s but got False"
            pytest.fail(msg)

    def test_maximum_constraint_t(self, solution: Solution) -> None:
        """Test case with maximum length t."""
        s = "a"  # Should be a single character that exists in t
        t = "a" * 10000
        result = solution.function_under_test(s, t)
        if not result:
            msg = "Expected True for maximum length t but got False"
            pytest.fail(msg)

    def test_all_characters_match_at_end(self, solution: Solution) -> None:
        """Test case where s characters are at the very end of t."""
        s = "xyz"
        t = "abcxyz"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for characters at end but got {result}"
            pytest.fail(msg)

    def test_interleaved_characters(self, solution: Solution) -> None:
        """Test case with interleaved characters in t."""
        s = "ace"
        t = "abcdef"
        result = solution.function_under_test(s, t)
        if not result:
            msg = f"Expected True for interleaved characters but got {result}"
            pytest.fail(msg)
            pytest.fail(msg)
