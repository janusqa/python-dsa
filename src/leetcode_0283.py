class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        if len(nums) < 1:
            return

        start_zero: int | None = None

        for i in range(len(nums)):
            if nums[i] == 0:
                if start_zero is None:
                    start_zero = i
                continue

            if start_zero is not None:
                nums[start_zero], nums[i] = nums[i], nums[start_zero]
                start_zero += 1

    def function_under_test(self, nums: list[int]) -> None:
        self.move_zeroes(nums)
