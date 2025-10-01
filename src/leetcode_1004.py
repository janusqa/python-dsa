class Solution:
    def longest_ones(self, nums: list[int], k: int) -> int:
        if len(nums) < 1:
            return 0

        if k < 0:
            return 0

        max_ones = 0
        flips = 0
        sw_low = 0

        for sw_high in range(len(nums)):
            if not (nums[sw_high] == 0 or nums[sw_high] == 1):
                return 0

            if nums[sw_high] == 0:
                flips += 1

            if flips <= k:
                continue

            # window is now invalid and contains more than k zeros.
            # Therefore we have a subsring. Process it where the
            # right side of the window is one less than sw_high
            max_ones = max(max_ones, sw_high - 1 - sw_low + 1)

            while flips > k:
                if nums[sw_low] == 0:
                    flips -= 1
                sw_low += 1

        # Process the final substring. It's not processed in the loop
        max_ones = max(max_ones, len(nums) - 1 - sw_low + 1)

        return max_ones

    def function_under_test(self, nums: list[int], k: int) -> int:
        return self.longest_ones(nums, k)


if __name__ == "__main__":
    print(
        Solution().longest_ones(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            3,
        ),
    )
