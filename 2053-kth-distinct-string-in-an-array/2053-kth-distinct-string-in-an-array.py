class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        store = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                store.append(arr[i])
        if len(store) >= k:
            return store[k-1]
        else:
            return ""    

                
            


        