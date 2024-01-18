class Solution:
    def backspaceCompare(self, s, t):
        szS = len(s)
        szT = len(t)
        sNew = self.findFinalString(s)
        tNew = self.findFinalString(t)
        return sNew == tNew

    def findFinalString(self, str):
        sz = len(str)
        hashCnt = 0
        res = []
        for indx in range(sz - 1, -1, -1):
            if str[indx] == '#':
                hashCnt += 1
            else:
                if hashCnt > 0:
                    hashCnt -= 1
                else:
                    res.append(str[indx])
        return ''.join(res[::-1])