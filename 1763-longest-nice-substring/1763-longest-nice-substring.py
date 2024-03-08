class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result=''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if all(s[k].swapcase() in s[i:j] for k in range(i,j)):
                    result = max(result,s[i:j],key=len)
        return result            
        