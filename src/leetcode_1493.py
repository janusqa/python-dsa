class Solution:
    def longest_subarray_sliding_window(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0

        sw_low = 0
        max_ones = 0
        zeros = 0

        for sw_high in range(len(nums)):
            if nums[sw_high] == 0:
                zeros += 1

            while zeros > 1:
                if nums[sw_low] == 0:
                    zeros -= 1
                sw_low += 1

            max_ones = max(max_ones, sw_high - sw_low)

        return max_ones

    def longest_subarray_use_prefixes(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0

        max_ones = 0

        prefixs: list[int] = [0] * len(nums)

        prefix = 0
        for i in range(len(nums)):
            prefixs[i] = prefix
            if nums[i] == 0:
                prefix = 0
            prefix += nums[i]

        suffix = 0
        for i in range(len(nums) - 1, -1, -1):
            max_ones = max(max_ones, prefixs[i] + suffix)
            if nums[i] == 0:
                suffix = 0
            suffix += nums[i]

        return max_ones

    def function_under_test(self, nums: list[int]) -> int:
        return self.longest_subarray_sliding_window(nums)


if __name__ == "__main__":
    print(Solution().longest_subarray_sliding_window([0, 0, 1, 1]))
