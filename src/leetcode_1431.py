class Solution:
    def kid_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        result: list[bool] = []
        max_candy = 0

        for i in range(len(candies)):
            max_candy = max(max_candy, candies[i])

        for i in range(len(candies)):
            result.append(candies[i] + extra_candies >= max_candy)

        return result
