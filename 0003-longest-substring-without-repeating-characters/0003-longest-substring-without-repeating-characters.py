class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " " or len(s) == 1: return 1
        i = 0
        j = i+1
        count = 0
        while j<len(s):
            if s[j] not in s[i:j]:
                j += 1
                count = max(count,len(s[i:j]))
              
            else:
                count = max(count,len(s[i:j]))
              
                i += 1
                j = i + 1
        return count        


        