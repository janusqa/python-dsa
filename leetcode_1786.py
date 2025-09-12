from pydantic import BaseModel


class Solution(BaseModel):
    def merge_alternately(self, word1: str, word2: str) -> str:
        output: str = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]

        return output


# if __name__ == "__main__":
#     print(Solution().mergeAlternately("abc", "pqr"))
