class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        low = float("inf")
        mid = float("inf")

        for i in range(len(nums)):
            if nums[i] > mid:
                return True

            if nums[i] <= low:
                low = nums[i]
            else:
                mid = nums[i]

        return False
