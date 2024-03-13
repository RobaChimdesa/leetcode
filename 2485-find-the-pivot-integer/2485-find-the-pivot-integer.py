class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        store=[]
        for i in range(n):
            store.append(i+1)
        j,k = 1,len(store)
        while j<k:
            if sum(store[:j+1]) == sum(store[j:k]):
                return store[j]
            else:
                j+=1
        return -1                



       
        