class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[: k])
        res = sum(nums[: k])
        

        for i in range(k,len(nums)):

            res += nums[i] - nums[i-k]

            max_sum = max(max_sum, res)

        return max_sum/k