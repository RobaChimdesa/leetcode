class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        continear=[]
        strnums = str(num)
        for i in range(len(strnums)-k+1):
            if int(strnums[i:k]) != 0 and num % int(strnums[i:k]) == 0:
                continear.append(int(strnums[i:k]))
            k+=1
        return len(continear)    






        