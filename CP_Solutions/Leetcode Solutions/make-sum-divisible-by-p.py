class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        mydict = {0:0}
        ans = float("inf")
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(1,len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        print(prefix_sum)

        k = prefix_sum[-1] % p

        for i in range(len(prefix_sum)):

            if (prefix_sum[i] - k) % p in mydict:

                ans = min(ans, i - (mydict[(prefix_sum[i] - k) % p]))

            mydict[prefix_sum[i] % p] = i

        return ans if ans < len(nums) else -1


