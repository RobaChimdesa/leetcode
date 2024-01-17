class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tot=sum(arr)
        ans=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                x=arr[i:j+1]
                if len(x)%2!=0:
                    ans+=sum(arr[i:j+1])
        return ans