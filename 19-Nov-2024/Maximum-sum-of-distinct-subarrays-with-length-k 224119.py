# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        curr_sum = 0
        max_sum = 0
        counter = Counter()
        for i,num in enumerate(nums):
            counter[num] += 1
            curr_sum  += num

            if i >= k:
                counter[nums[i-k]] -= 1
                if counter[nums[i-k]] == 0:
                    del counter[nums[i-k]]
                curr_sum -= nums[i-k]

            if len(counter) == k:
                max_sum = max(max_sum , curr_sum)            
        return max_sum