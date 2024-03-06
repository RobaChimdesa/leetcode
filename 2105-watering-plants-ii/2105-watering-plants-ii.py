class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refill = 0 
        i, j = 0, len(plants)-1
        canA, canB = capacityA, capacityB
        while i < j: 
            if canA < plants[i]: refill += 1; canA = capacityA
            canA -= plants[i]
            if canB < plants[j]: refill += 1; canB = capacityB
            canB -= plants[j]
            i, j = i+1, j-1
        if i == j and max(canA, canB) < plants[i]: refill += 1
        return refill 