class Solution:
    def qs(self, arr: list[int], low: int, high: int) -> None:
        if low >= high:
            return

        pivot_idx: int = self.partition(arr, low, high)

        self.qs(arr, low, pivot_idx - 1)
        self.qs(arr, pivot_idx + 1, high)

    def partition(self, arr: list[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[i], arr[high] = arr[high], arr[i]

        return i

    def quick_sort(self, arr: list[int]) -> None:
        self.qs(arr, 0, len(arr) - 1)
