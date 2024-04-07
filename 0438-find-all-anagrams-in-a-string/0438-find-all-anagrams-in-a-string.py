class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        counter=0
        for i in range(len(s)-len(p)+1):
            x=sorted(s[i:i+(len(p))])
            p=sorted(p)
            if(x==p):
                counter+=1
                ans.append(i)
        return ans      