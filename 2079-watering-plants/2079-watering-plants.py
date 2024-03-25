class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step,original = 0,capacity

        for i,plant in enumerate(plants):

            if plants[i] <= capacity:
                step+=1
                
            else:

                capacity = original
                step+=2*i + 1
            capacity-=plants[i]
        return step
        