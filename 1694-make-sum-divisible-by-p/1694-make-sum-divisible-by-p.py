class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        remainder = summ % p
        hashmap = {0:-1} #current cumulative modulo p with index

        if remainder == 0:
            return 0

        cumulative = 0
        ans = float("inf")

        for i , num in enumerate(nums):
            cumulative += num
            curr_remainder = cumulative % p

            if (cumulative - remainder) % p in hashmap:
                ans = min(ans, i - hashmap[(cumulative - remainder) % p])

            hashmap[curr_remainder] = i

        return -1 if ans == float("inf") or ans == len(nums)else ans