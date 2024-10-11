class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        for j in range(n-1,-1,-1):
            for i in range(n):
                if nums[j] >= nums[i]:
                    return j-i
        
        return 0
        



            
        
        