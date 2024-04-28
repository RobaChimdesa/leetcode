class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        """
        j=0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i]

            if nums[j] !=0:
                j+=1
        Do not return anything, modify nums in-place instead.
        """
        read = 0 
        write = 0
        while read < len(nums):

            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
                write+=1
            read+=1
        return nums        

                
       


            
        