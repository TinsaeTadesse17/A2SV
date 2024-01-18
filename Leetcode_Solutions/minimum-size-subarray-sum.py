class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        right = 0
        left = 0
        summ = 0
        ans = float("inf")

        for right in range(len(nums)):

            summ += nums[right]


            while summ >= target:
                ans = min(ans,right-left+1)
                summ -= nums[left]
                left += 1

        return ans if ans != float("inf") else 0
