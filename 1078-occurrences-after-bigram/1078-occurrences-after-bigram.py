class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        txt = text.split()
        store=[]
        for i in range(len(txt)-2):
            if txt[i] == first and txt[i+1] == second:
                store.append(txt[i+2])

       
        return store