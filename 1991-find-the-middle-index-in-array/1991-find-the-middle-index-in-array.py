class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        allSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if allSum - leftSum - nums[i] == leftSum:
                return i
            else:
                leftSum += nums[i]
        return -1            


            
        