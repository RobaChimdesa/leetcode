class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=""
        y=[]
        for i in range(len(strs)):
            y.append(len(strs[i]))
        for i in range(min(y)):
            cnt=1
            for j in range(1,len(strs)):
                if(strs[0][i]==strs[j][i]):
                    cnt+=1
            if(cnt==len(strs)):
                x+=strs[0][i]
            else:
                break
        return x
                
        