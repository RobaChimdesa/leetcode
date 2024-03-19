class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        c = 0
        n=len(nums)
        if n == 0: return 0
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    c = max(c,nums[i] ^ nums[j])
        return c            
        