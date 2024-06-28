class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n%2 != 0:
            return nums1[(n//2)]
        else:
            m = int(n/2)
            return (nums1[m]+nums1[m-1])/2

       