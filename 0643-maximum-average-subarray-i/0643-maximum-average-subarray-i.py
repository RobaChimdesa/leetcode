class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        totalsum = maxsum=sum(nums[0:k])
        for i in range(k,len(nums)):
            totalsum+=nums[i]
            totalsum-=nums[i-k]
            maxsum=max(maxsum,totalsum)
        return maxsum/k    
        


        