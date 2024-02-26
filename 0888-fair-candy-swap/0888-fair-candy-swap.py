class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        x=(sum(aliceSizes)-sum(bobSizes)) / 2
        sets = set(aliceSizes)
        for y in bobSizes:
            if y+ x in sets:
                return [y+x,y]
        