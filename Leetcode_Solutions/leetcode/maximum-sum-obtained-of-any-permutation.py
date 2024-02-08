class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        ans= [0] * (len(nums) + 1)
        res = 0
        
        for start, end in requests:
            ans[start] += 1
            ans[end + 1] -= 1

        for i in range(1,len(nums)):
            ans[i] = ans[i-1] + ans[i]

        ans = ans[:-1]

        ans.sort()
        nums.sort()

        for i in range(len(ans)):
            res += ans[i] * nums[i]

        return res % (pow(10,9) + 7)
