class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr_sum = 1  
        ans = 0  
        i = 0  
        
        while curr_sum <= n:
            if i < len(nums) and nums[i] <= curr_sum:
                curr_sum += nums[i]  
                i += 1  
            else:
                # We need a patch equal to curr_sum
                curr_sum += curr_sum  
                ans += 1  

        return ans