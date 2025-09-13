class Solution:
    def bubble_sort(self, arr: list[int]) -> None:
        n = len(arr) - 1

        while n > 0:
            for i in range(n):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

            n -= 1
