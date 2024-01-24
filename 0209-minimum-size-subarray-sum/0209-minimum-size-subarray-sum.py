class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # i,j = 0,1
        # result = float("inf")
        # while i<j and j<=len(nums):
        #     if sum(nums[i:j]) >= target:
        #         result = min(result,len(nums[i:j]))
        #         i+=1
        #     else:
        #         j+=1
        # return 0 if result == float("inf") else result           
        j ,total = 0,0
        result = float("inf")
        for i in range(len(nums)):
            total+=nums[i]
            while total >= target:
                result = min(result,i-j+1)
                total-=nums[j]
                j+=1
        return 0 if result == float("inf") else result          
        