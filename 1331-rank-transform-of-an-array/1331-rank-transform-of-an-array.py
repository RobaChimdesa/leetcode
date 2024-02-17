class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        f_lst=[]
        arr1 = sorted(list(set(arr)))
        for i in range(len(arr1)):
            d[arr1[i]] = i+1
        for i in arr:
            f_lst.append(d[i])
        return f_lst
        