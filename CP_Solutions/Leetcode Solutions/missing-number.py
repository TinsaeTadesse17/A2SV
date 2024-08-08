class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set()
        ans = []
        for i in range(0,len(nums)+1):
          num.add(i)
        nums = set(nums)
        ans = list(num-nums)
        return ans[0]

        