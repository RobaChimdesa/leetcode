class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        result=sum(nums[:3])
        for i in range(len(nums)-2):
            n = i + 1
            m =  len(nums)-1
            while n<m:
                heresum=nums[i] + nums[n] + nums[m]
                if abs(heresum - target) < abs(result-target):

                    result=heresum
                if heresum < target:
                    n+=1
                else:

                    m-=1
        return result                    

        