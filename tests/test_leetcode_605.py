import pytest

from leetcode_605 import Solution


class TestCanPlaceFlowers:
    @pytest.fixture
    def solution(self) -> Solution:
        """Return a Solution instance for testing."""
        return Solution()

    def test_basic_case_where_one_flower_can_be_planted(
        self,
        solution: Solution,
    ) -> None:
        """Test basic case where one flower can be planted."""
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_case_where_two_flowers_cannot_be_planted(self, solution: Solution) -> None:
        """Test case where two flowers cannot be planted."""
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        result = solution.can_place_flowers(flowerbed, n)
        expected = False
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_planting_in_completely_empty_flowerbed(self, solution: Solution) -> None:
        """Test planting in completely empty flowerbed."""
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_planting_in_already_full_flowerbed(self, solution: Solution) -> None:
        """Test planting in already full flowerbed."""
        flowerbed = [1, 0, 1, 0, 1]
        n = 1
        result = solution.can_place_flowers(flowerbed, n)
        expected = False
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_edge_cases_with_single_plot_flowerbeds(self, solution: Solution) -> None:
        """Test edge cases with single plot flowerbeds."""
        single_empty_result = solution.can_place_flowers([0], 1)
        single_empty_expected = True
        if single_empty_result != single_empty_expected:
            error_msg = f"Single empty: Expected {single_empty_expected}, got {single_empty_result}"
            pytest.fail(error_msg)

        single_planted_result = solution.can_place_flowers([1], 1)
        single_planted_expected = False
        if single_planted_result != single_planted_expected:
            error_msg = f"Single planted: Expected {single_planted_expected}, got {single_planted_result}"
            pytest.fail(error_msg)

    def test_planting_zero_flowers_should_always_succeed(
        self,
        solution: Solution,
    ) -> None:
        """Test planting zero flowers (should always succeed)."""
        flowerbed = [1, 0, 1, 0, 1]
        n = 0
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_planting_in_alternating_pattern(self, solution: Solution) -> None:
        """Test planting in alternating pattern."""
        flowerbed = [0, 1, 0, 1, 0, 1, 0]
        n = 1
        result = solution.can_place_flowers(flowerbed, n)
        expected = False  # Corrected: Cannot plant anywhere due to adjacent flowers
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_with_large_flowerbed_near_constraint_limit(
        self,
        solution: Solution,
    ) -> None:
        """Test with large flowerbed near constraint limit."""
        large_flowerbed = [0] * 20000
        large_n = 10000
        result = solution.can_place_flowers(large_flowerbed, large_n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_planting_more_flowers_than_physically_possible(
        self,
        solution: Solution,
    ) -> None:
        """Test planting more flowers than physically possible."""
        flowerbed = [0, 0, 0, 0, 0]
        n = 10
        result = solution.can_place_flowers(flowerbed, n)
        expected = False
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_complex_planting_pattern(self, solution: Solution) -> None:
        """Test a more complex planting pattern."""
        flowerbed = [1, 0, 0, 0, 0, 1]
        n = 2
        result = solution.can_place_flowers(flowerbed, n)
        expected = False  # Corrected: Can only plant 1 flower (either position 2 or 3)
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_algorithm_does_not_violate_adjacent_rule(self, solution: Solution) -> None:
        """Test that solution doesn't violate adjacent rule."""
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_minimum_length_flowerbed(self, solution: Solution) -> None:
        """Test with minimum length flowerbed according to constraints."""
        flowerbed = [0]
        n = 1
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_maximum_n_value(self, solution: Solution) -> None:
        """Test with maximum n value according to constraints."""
        flowerbed = [0] * 20000
        n = 20000
        result = solution.can_place_flowers(flowerbed, n)
        expected = False
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_consecutive_planting_scenario(self, solution: Solution) -> None:
        """Test planting multiple flowers in consecutive empty spots."""
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_three_consecutive_empty_spots(self, solution: Solution) -> None:
        """Test planting in three consecutive empty spots."""
        flowerbed = [0, 0, 0]
        n = 1  # Corrected: Can only plant 1 flower in the middle
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_four_consecutive_empty_spots(self, solution: Solution) -> None:
        """Test planting in four consecutive empty spots."""
        flowerbed = [0, 0, 0, 0]
        n = 2  # Corrected: Can plant at positions 1 and 3
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_five_consecutive_empty_spots(self, solution: Solution) -> None:
        """Test planting in five consecutive empty spots."""
        flowerbed = [0, 0, 0, 0, 0]
        n = 3  # Corrected: Can plant at positions 0, 2, 4
        result = solution.can_place_flowers(flowerbed, n)
        expected = True
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_pattern_with_edges(self, solution: Solution) -> None:
        """Test planting with edge cases at both ends."""
        flowerbed = [0, 0, 1, 0, 0]
        n = 2
        result = solution.can_place_flowers(flowerbed, n)
        expected = True  # Can plant at position 0 and position 4
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)

    def test_no_possible_planting_due_to_adjacency(self, solution: Solution) -> None:
        """Test case where no planting is possible due to adjacency."""
        flowerbed = [1, 0, 1]
        n = 1
        result = solution.can_place_flowers(flowerbed, n)
        expected = False
        if result != expected:
            error_msg = f"Expected {expected}, got {result}"
            pytest.fail(error_msg)
