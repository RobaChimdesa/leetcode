class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            res = [0] * (high - low + 1)
            i = low
            j = mid + 1
            k = 0
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    res[k] = nums[i]
                    i += 1
                    k += 1
                else:
                    res[k] = nums[j]
                    j += 1
                    k += 1
            while i <= mid:
                res[k] = nums[i]
                i += 1
                k += 1
            while j <= high:
                res[k] = nums[j]
                j += 1
                k += 1
            for x in range(len(res)):
                nums[low + x] = res[x]
        def mergeSort(low, high):
            if low < high:
                mid = low + (high - low) // 2
                mergeSort(low, mid)
                mergeSort(mid + 1, high)
                merge(low, mid, high)
        mergeSort(0, len(nums) - 1)
        return nums