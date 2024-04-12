class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # min_operation = float('inf')
        min_operation  = n
        
        for i in range(n-k+1):
            black_ka_count = blocks[i:i+k].count('B')
            needed = k - black_ka_count
            min_operation = min(min_operation, needed)
        return  min_operation if  min_operation != float('inf') else 0
            