from collections import Counter
class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        check=Counter(arr)
        result=[]
        for i in arr:
            if check[i] == 2 and i not in result:
                result.append(i)
        return result        
        