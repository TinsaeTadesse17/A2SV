# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
  def maxWidthRamp(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    stack = []

    for i, num in enumerate(nums):
      if not stack or num <= nums[stack[-1]]:
        stack.append(i)

    for i in range(n-1,-1,-1):
      while stack and nums[i] >= nums[stack[-1]]:
        ans = max(ans, i - stack.pop())

    return ans