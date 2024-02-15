class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        answer = [0] * len(nums)
        for i in nums:
            if i % 2 == 0:
                answer[l] = i
                l+= 1
            else:
                answer[r] = i
                r-= 1
        return answer