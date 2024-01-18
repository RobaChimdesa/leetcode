class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # solve using dictionary
        store={}

        for i in range(len(nums)):
            if nums[i] in store and abs(store[nums[i]]-i) <=k:
                return True
            store[nums[i]] = i
        return False        
        