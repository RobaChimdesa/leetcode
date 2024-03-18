class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        minn = float('inf')
        white = 0
        for i in range(n-k+1):
            black_ka_count = blocks[i:i+k].count('B')
            needed = k - black_ka_count
            minn = min(minn, needed)
        return minn if minn != float('inf') else 0
            