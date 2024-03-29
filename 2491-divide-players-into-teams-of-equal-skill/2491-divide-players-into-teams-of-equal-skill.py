class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        if len(skill)%2 != 0:
            return -1
        sm = skill[0]+skill[-1]    
        sumChemistry = skill[0]*skill[-1]

        i,j = 1,len(skill)-2
     
        while i<j:
            x = skill[i] + skill[j]
            y = skill[i] * skill[j]
            if x == sm:
                sumChemistry+=y
                i+=1
                j-=1
            else:
                return -1
        return sumChemistry                 




        