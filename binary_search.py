class Solution:
    def binary_search(self, haystack: list[int], needle: int) -> bool:
        low = 0
        high = len(haystack)

        while low < high:
            m = low + (high - low) // 2
            v = haystack[m]

            if needle == v:
                return True

            if needle > v:
                low = m + 1
            else:
                high = m

        return False
