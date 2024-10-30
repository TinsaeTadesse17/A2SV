class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # LIS
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # LDS
        LDS = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        
        # longest mountain
        max_mountain = 0
        for i in range(1, n - 1):
            if LIS[i] > 1 and LDS[i] > 1:  # valid 
                max_mountain = max(max_mountain, LIS[i] + LDS[i] - 1)
        
        return n - max_mountain
