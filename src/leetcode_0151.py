class Solution:
    """Use iterative solution to find a word and add it to the result."""

    def reverse_words(self, s: str) -> str:
        s_list = list(s)
        result: list[str] = []

        i = len(s_list) - 1

        while i >= 0:
            if s_list[i] == " ":
                i -= 1
                continue

            if len(result) > 0:
                result.append(" ")

            word: list[str] = []
            while s_list[i] != " ":
                word.append(s_list[i])
                i -= 1
                if i < 0:
                    break

            self.reverse_slice(word, 0, len(word) - 1)
            result.extend(word)

        return "".join(result)

    def reverse_slice(self, s_list: list[str], low: int, high: int) -> None:
        while low < high:
            s_list[low], s_list[high] = s_list[high], s_list[low]
            low += 1
            high -= 1


###


class SolutionSolutionIterativeWithNoExtraBuffer:
    """Use iterative solution to find a word and add it to the result."""

    def reverse_words(self, s: str) -> str:
        s_list = list(s)
        result: list[str] = []

        # trim entire list
        s_list_len = self.trim_spaces(s_list)

        # reverse entire list
        self.reverse_slice(s_list, 0, s_list_len - 1)

        low = 0
        high = low

        while low < s_list_len:
            if s_list[low] == " ":
                low += 1
                continue

            high = low

            while high < s_list_len:
                if s_list[high] != " ":
                    high += 1
                    continue
                break

            self.reverse_slice(s_list, low, high - 1)

            low = high

        return "".join(s_list[0:s_list_len])

    def trim_spaces(self, s_list: list[str]) -> int:
        """Removes extra spaces in-place and returns the new length."""
        write_idx = 0
        read_idx = 0
        n = len(s_list)

        # 1. Skip leading spaces
        while read_idx < n and s_list[read_idx] == " ":
            read_idx += 1

        # 2. Process all characters
        while read_idx < n:
            # If it's a non-space character, or a single space
            if s_list[read_idx] != " ":
                s_list[write_idx] = s_list[read_idx]
                write_idx += 1
            elif write_idx > 0 and s_list[write_idx - 1] != " ":
                s_list[write_idx] = " "
                write_idx += 1

            read_idx += 1

        # 3. Handle trailing space
        if write_idx > 0 and s_list[write_idx - 1] == " ":
            write_idx -= 1

        return write_idx

    def reverse_slice(self, s_list: list[str], low: int, high: int) -> None:
        while low < high:
            s_list[low], s_list[high] = s_list[high], s_list[low]
            low += 1
            high -= 1


###


class SolutionRecursiveDFS:
    """Use recursive dfs to find a word and return that word which is added to final result."""

    def reverse_words(self, s: str) -> str:
        s_list = list(s)
        visited: set[int] = set()
        result: list[str] = []

        for i in reversed(range(len(s_list))):
            word = self.get_word(s_list, i, visited)
            if len(word) > 0:
                if len(result) > 0:
                    result.append(" ")
                self.reverse_slice(word, 0, len(word) - 1)
                result.extend(word)

        return "".join(result)

    def get_word(
        self,
        s_list: list[str],
        i: int,
        visited: set[int],
    ) -> list[str]:
        row_inbounds = 0 <= i < len(s_list)
        if not row_inbounds:
            return []

        if s_list[i] == " ":
            return []

        key = i
        if key in visited:
            return []

        visited.add(key)

        result = [s_list[i]]

        result.extend(self.get_word(s_list, i - 1, visited))

        return result

    def reverse_slice(self, s_list: list[str], low: int, high: int) -> None:
        while low < high:
            s_list[low], s_list[high] = s_list[high], s_list[low]
            low += 1
            high -= 1
