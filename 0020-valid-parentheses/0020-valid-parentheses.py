class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in mydict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if mydict[a] != s[i]:
                        return False
        return stack == []                

