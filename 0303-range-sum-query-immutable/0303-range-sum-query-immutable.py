class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]

        for num in nums:
            self.prefixSum.append(self.prefixSum[-1]+num)
        print (self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prefixSum[left]
       
        rightsum = self.  prefixSum[right+1]
        print(rightsum)
        return rightsum - leftsum

       
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)