class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(heights)
        for i in range(n):
            minidx = i
            for j in range(i+1,n):
                if heights[j] > heights[minidx]:
                    minidx = j
            heights[i],heights[minidx] = heights[minidx], heights[i]
            names[i],names[minidx] = names[minidx],names[i]
        return names    

       