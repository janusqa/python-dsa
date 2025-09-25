class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True

        if len(t) < 1:
            return False

        s_ptr = 0

        for t_ptr in range(len(t)):
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1

            if s_ptr > len(s) - 1:
                return True

        return False

    def function_under_test(self, s: str, t: str) -> bool:
        return self.is_subsequence(s, t)
