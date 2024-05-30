class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = list(set(word))
        i = 0
        count = 0
        for i in range(i,len(word)-1):
            if word[i].isupper() and word[i].lower() in word[i+1:]:
                count += 1
                i  += 1
            
            elif word[i].islower() and word[i].upper() in word[i+1:]:
                count += 1
                i += 1
        return count        


