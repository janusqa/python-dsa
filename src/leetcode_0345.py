class Solution:
    vowels = frozenset(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"))

    def reverse_vowels(self, s: str) -> str:
        s_list = list(s)

        low = 0
        high = len(s_list) - 1

        while low < high:
            if s_list[low] in Solution.vowels and s_list[high] in Solution.vowels:
                s_list[low], s_list[high] = s_list[high], s_list[low]
                low += 1
                high -= 1
                continue

            if s_list[low] not in Solution.vowels:
                low += 1

            if s_list[high] not in Solution.vowels:
                high -= 1

        return "".join(s_list)
