class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countmap={}
        left=0
        result=0
        maxfrq=0
        for right in range(len(s)):
            countmap[s[right]] = 1+countmap.get(s[right],0)
            maxfrq=max(maxfrq,countmap[s[right]])

            while (right-left+1)-maxfrq > k:
                countmap[s[left]]-=1
                left+=1

            result = max(result,right-left+1)
        return result        

        





     