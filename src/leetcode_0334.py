class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        low = float("inf")
        high = low

        for i in range(len(nums)):
            if nums[i] <= low:
                low = nums[i]
            elif nums[i] <= high:
                high = nums[i]

            if nums[i] > high:
                return True

        return False

    def function_under_test(self, nums: list[int]) -> bool:
        return self.increasing_triplet(nums)
