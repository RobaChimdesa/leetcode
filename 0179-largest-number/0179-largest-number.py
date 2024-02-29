class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x+y > y+x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumKey)
        largest_sum = ''.join(nums)

        return "0" if largest_sum[0] == "0" else largest_sum
