class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_multiple, suffix_multiple = [1] * len(nums), [1] * len(nums)
        ans = []
        
        for i in range(1, len(nums)):
            prefix_multiple[i] = prefix_multiple[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_multiple[i] = suffix_multiple[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            ans.append(prefix_multiple[i] * suffix_multiple[i])

        return ans
