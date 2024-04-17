class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 0
        last = {}
        s = set()
        l = 0; r =0
        nums = fruits
        for r in range(len(nums)):
            s.add(nums[r])
            last[nums[r]] = r
            if len(s) > 2:
                a = min(s,key=lambda x:last[x])
                s.remove(a)
                l = last[a] + 1
            best = max(best,r-l+1)
        return best        
        
        