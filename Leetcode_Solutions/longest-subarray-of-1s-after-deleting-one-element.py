class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    ans = 0
    count = 0

    left = 0
    for right, num in enumerate(nums):
      if num == 0:
        count += 1
      while count == 2:
        if nums[left] == 0:
          count -= 1
        left += 1
      ans = max(ans, right - left)

    return ans