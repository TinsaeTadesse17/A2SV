class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key = lambda x : x / (10 ** len(str(x)) - 1) , reverse = True)
        nums = [str(num) for num in nums]
        return str(int(''.join(nums)))