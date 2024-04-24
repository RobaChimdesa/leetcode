class Solution:
    def tribonacci(self, n: int) -> int:
        zero,one,two = 0,1,1
        if n==0:
            return zero
        if n<3:
            return one

        for i in range(3,n+1):
            curr = zero+one+two
            zero,one,two = one,two,curr

        return two