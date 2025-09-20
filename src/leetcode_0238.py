class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        answer: list[int] = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

    def function_under_test(self, nums: list[int]) -> list[int]:
        return self.product_except_self(nums)
