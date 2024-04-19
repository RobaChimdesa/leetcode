class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum,totalSum = 0,sum(nums)
        for i in range(len(nums)):
            rightSum = totalSum-nums[i]-leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1        
        
        