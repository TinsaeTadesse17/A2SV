class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        curSum = 0

        for num in nums:

            if curSum < 0:
                curSum = 0
            curSum += num
            max_subarray = max(curSum,max_subarray)
        
        return max_subarray