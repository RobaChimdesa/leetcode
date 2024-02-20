class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n=min(len(nums1),len(nums2))
        bothnums=nums1 if len(nums1) == n or len(nums1) == len(nums2) else nums2
        allA=nums2 if len(nums1)== len(nums2) or len(nums2)>n else nums1
        intersecion=set()
        for i in range(n):

            if bothnums[i] in allA:

                intersecion.add(bothnums[i])
        return list(intersecion)
        