class Solution:
    def firstUniqChar(self, s: str) -> int:
        x=len(s)
        for i in range(x):
            if s[i] not in s[i+1:x+1] and s[i] not in s[0:i]:
                return i
        return -1    
        