import pytest


class Solution:
    def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extra_candies >= max_candies)
        return result


@pytest.mark.parametrize(
    ("candies", "extra_candies", "expected"),
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ([1, 1], 1, [True, True]),
        ([5, 5, 5], 0, [True, True, True]),
        ([1, 2, 3, 4, 5], 2, [False, False, True, True, True]),
    ],
)
def test_kids_with_candies(
    candies: list[int],
    extra_candies: int,
    expected: list[bool],
) -> None:
    solution = Solution()
    actual = solution.kids_with_candies(candies, extra_candies)

    if actual != expected:
        error_msg = f"Test failed for candies={candies}, extra_candies={extra_candies}. Expected {expected}, got {actual}"
        pytest.fail(error_msg)


def test_single_kid() -> None:
    """Test edge case with minimum n=2 (though constraints say n>=2, this tests robustness)."""
    solution = Solution()
    actual = solution.kids_with_candies([5, 3], 3)
    expected: list[bool] = [True, True]

    if actual != expected:
        error_msg = f"Test failed for two kids. Expected {expected}, got {actual}"
        pytest.fail(error_msg)


def test_all_kids_get_max() -> None:
    solution = Solution()
    actual = solution.kids_with_candies([3, 3, 3, 3], 2)
    expected: list[bool] = [True, True, True, True]

    if actual != expected:
        error_msg = (
            f"Test failed for all kids getting max. Expected {expected}, got {actual}"
        )
        pytest.fail(error_msg)


def test_no_extra_candies() -> None:
    solution = Solution()
    actual = solution.kids_with_candies([1, 5, 3], 0)
    expected: list[bool] = [False, True, False]

    if actual != expected:
        error_msg = (
            f"Test failed for no extra candies. Expected {expected}, got {actual}"
        )
        pytest.fail(error_msg)


def test_large_extra_candies() -> None:
    solution = Solution()
    actual = solution.kids_with_candies([1, 2, 3], 10)
    expected: list[bool] = [True, True, True]

    if actual != expected:
        error_msg = (
            f"Test failed for large extra candies. Expected {expected}, got {actual}"
        )
        pytest.fail(error_msg)


def test_minimum_constraints() -> None:
    """Test the minimum constraints: n=2, candies[i]=1, extra_candies=1."""
    solution = Solution()
    actual = solution.kids_with_candies([1, 1], 1)
    expected: list[bool] = [True, True]

    if actual != expected:
        error_msg = (
            f"Test failed for minimum constraints. Expected {expected}, got {actual}"
        )
        pytest.fail(error_msg)


def test_maximum_constraints() -> None:
    """Test near maximum constraints."""
    solution = Solution()
    actual = solution.kids_with_candies([100, 50, 75, 25, 1], 50)
    expected: list[bool] = [True, True, True, False, False]  # Corrected!

    if actual != expected:
        error_msg = (
            f"Test failed for maximum constraints. Expected {expected}, got {actual}"
        )
        pytest.fail(error_msg)
