class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dict1, dict2 = {}, {}

        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        
        i, j, n, ans = 0, 0, len(nums), 0

        while i < n:
            dict2[nums[i]] = dict2.get(nums[i], 0) + 1

            while len(dict2) == len(dict1):
                ans += (n - i)
                dict2[nums[j]] -= 1
                if dict2[nums[j]] == 0:
                    del dict2[nums[j]]
                j += 1
            i += 1
        
        return ans
    