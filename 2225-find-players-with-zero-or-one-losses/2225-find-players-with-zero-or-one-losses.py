class Solution:
    def findWinners(self, matches):
        lose = defaultdict(int)
        print(lose)
        zero,one = [],[]
        for game in matches:
            lose[game[0]] += 0
            lose[game[1]] += 1
        zero = sorted([k for k,l in lose.items() if l == 0])
        one =  sorted([k for k,l in lose.items() if l ==1])
        return [zero,one]    
           
                 
                          
            

