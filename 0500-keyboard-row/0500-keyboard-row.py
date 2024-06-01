class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        FristRow = "qwertyuiop"
        SecondRow = "asdfghjkl"
        ThirdRow = "zxcvbnm"
        store = []
        nums = {}
        for num in words:
            nums[num.lower()] = num
      

        ans = []
        for char in words:
            
            char = char.lower()
            if len(char) == 1:store.append(char)
            elif char[0] in FristRow:
               
                for i in range(1,len(char)):
                    if char[i] not in FristRow:
                        break
                    else:
                        if i == len(char)-1:
                            store.append(char)
                               
                
            elif char[0] in SecondRow:
                
                for i in range(1,len(char)):
                    if char[i] not in SecondRow:
                        break
                    else:
                         if i == len(char)-1:
                            store.append(char) 
                              
                    
            else:
            
                for i in range(1,len(char)):
                    if char[i] not in ThirdRow:
                        break
                    else:
                         if i == len(char)-1:
                            store.append(char) 
                           
        for j in store:
            ans.append(nums[j])             
                 
        return ans
        

        