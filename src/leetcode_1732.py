class Solution:
    def largesta_altitude(self, gain: list[int]) -> int:
        if len(gain) < 1:
            return 0

        max_altitude = 100
        hightest_altitude = 0
        current_altitude = 0

        for i in range(len(gain)):
            if not (-max_altitude <= gain[i] <= max_altitude):
                return 0

            current_altitude += gain[i]
            hightest_altitude = max(hightest_altitude, current_altitude)

        return hightest_altitude

    def function_under_test(self, gain: list[int]) -> int:
        return self.largesta_altitude(gain)


if __name__ == "__main__":
    print(Solution().largesta_altitude([5, -3, 4, -2, 3, -1]))
