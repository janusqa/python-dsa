class Solution:
    def max_area(self, height: list[int]) -> int:
        min_containers = 2
        if len(height) < min_containers:
            return 0

        maximum_area = 0
        low = 0
        high = len(height) - 1

        while low < high:
            current_area = min(height[low], height[high]) * (high - low)

            maximum_area = max(maximum_area, current_area)

            if height[low] >= height[high]:
                high -= 1
            else:
                low += 1

        return maximum_area

    def function_under_test(self, height: list[int]) -> int:
        return self.max_area(height)
