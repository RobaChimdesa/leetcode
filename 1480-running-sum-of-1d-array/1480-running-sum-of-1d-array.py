class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=[nums[0]]
        for i in range(1,len(nums)):
            n.append(n[i-1]+nums[i])
        return n