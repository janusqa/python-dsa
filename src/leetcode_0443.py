class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) < 1:
            return 0

        read_pos = 0
        write_pos = 0
        last_char_read = chars[0]
        last_char_count = 0
        cache_empty = False

        while read_pos < len(chars):
            if chars[read_pos] == last_char_read:
                last_char_count += 1
                read_pos += 1
                cache_empty = False
                continue

            write_pos = self.write(chars, last_char_read, last_char_count, write_pos)
            cache_empty = True

            last_char_read = chars[read_pos]
            last_char_count = 0

        if not cache_empty:
            write_pos = self.write(chars, last_char_read, last_char_count, write_pos)
            cache_empty = True

        return write_pos

    def write(
        self,
        chars: list[str],
        char: str,
        char_count: int,
        write_pos: int,
    ) -> int:
        chars[write_pos] = char
        write_pos += 1

        if char_count > 1:
            for c in str(char_count):
                chars[write_pos] = c
                write_pos += 1

        return write_pos

    def function_under_test(self, chars: list[str]) -> int:
        return self.compress(chars)
