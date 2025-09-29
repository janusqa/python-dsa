class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0

        if k < 1 or k > len(s):
            return 0

        max_v = 0
        running_sum = 0
        sw_low = 0
        vowels = {"a", "e", "i", "o", "u"}

        for sw_high in range(len(s)):
            if sw_high < k - 1:
                running_sum += 1 if s[sw_high] in vowels else 0
                continue

            running_sum += 1 if s[sw_high] in vowels else 0

            max_v = max(max_v, running_sum)

            running_sum -= 1 if s[sw_low] in vowels else 0
            sw_low += 1

        return max_v

    def function_under_test(self, s: str, k: int) -> int:
        return self.max_vowels(s, k)
