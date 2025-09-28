class Solution:
    def max_operations(self, nums: list[int], k: int) -> int:
        min_valid_k = 2
        min_input_size = 2

        if len(nums) < min_input_size:
            return 0

        if k < min_valid_k:
            return 0

        pairs: dict[int, int] = {}
        operations = 0

        for i in range(len(nums)):
            if nums[i] >= k:
                continue

            partner = k - nums[i]

            if partner in pairs and pairs[partner] > 0:
                pairs[partner] -= 1
                operations += 1
            elif nums[i] not in pairs:
                pairs[nums[i]] = 1
            else:
                pairs[nums[i]] += 1

        return operations

    def function_under_test(self, nums: list[int], k: int) -> int:
        return self.max_operations(nums, k)
