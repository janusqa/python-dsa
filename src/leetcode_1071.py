class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        gcd = str1

        if len(str2) < len(str1):
            gcd = str2

        gcd_length = len(gcd)

        while gcd_length > 0:
            if self.is_divisor(str1, gcd) and self.is_divisor(str2, gcd):
                return gcd
            gcd_length -= 1
            gcd = gcd[:gcd_length]

        return ""

    def is_divisor(self, input_str: str, gcd: str) -> bool:
        low = 0
        high = len(gcd)

        while high < len(input_str):
            if gcd != input_str[low:high]:
                break

            low = high
            high = low + len(gcd)

        return gcd == input_str[low:high]
