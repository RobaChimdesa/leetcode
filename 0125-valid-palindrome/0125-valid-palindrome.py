class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=''.join(filter(str.isalnum,s))
        s=s.lower()
        i=0
        j=len(s)-1
        while j>i:


            if s[i] == s[j]:

                i+=1
                j-=1
            else:

                return False
        return True   
        
        