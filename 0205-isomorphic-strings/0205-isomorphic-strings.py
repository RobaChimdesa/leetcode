class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     if s.count(s[i]) != t.count(t[i]):
        #         return False
            
        # return True
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))


    