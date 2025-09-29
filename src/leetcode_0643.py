class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        if k < 1:
            return 0

        if len(nums) < k:
            return 0

        max_sum = -float("inf")
        sw_low = 0
        running_sum = 0

        for sw_high in range(len(nums)):
            if sw_high < k - 1:
                running_sum += nums[sw_high]
                continue

            running_sum += nums[sw_high]

            max_sum = max(max_sum, running_sum)

            running_sum -= nums[sw_low]
            sw_low += 1

        return max_sum / k

    def function_under_test(self, nums: list[int], k: int) -> float:
        return self.find_max_average(nums, k)
