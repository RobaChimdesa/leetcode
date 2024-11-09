class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while left<=right and right < len(nums):
            if (nums[left] != nums[right]): 
                nums[left+1]=nums[right]
                left +=1
            else:
                right += 1
        return left+1           
        