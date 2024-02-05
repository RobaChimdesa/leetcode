class Solution:
    def countBits(self, n: int) -> List[int]:
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i >> 1] + (i & 1)
        return s