class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # brute force
        prev_len = 0
        cur_len = 1
        # max_len = 0
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_len += 1
            else:
                prev_len = cur_len
                cur_len = 1
            if prev_len >= cur_len:
                count += 1

        return count