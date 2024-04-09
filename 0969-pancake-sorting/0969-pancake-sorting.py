class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        a = arr.copy()
        ans = []
        for x in range(n,0,-1):
            
            idx = a.index(x)
         
            ans.extend([idx+1, x])
          
            a[:idx+1] = list(reversed(a[:idx+1]))
            a[:x] = list(reversed(a[:x]))
           
        return ans    


        