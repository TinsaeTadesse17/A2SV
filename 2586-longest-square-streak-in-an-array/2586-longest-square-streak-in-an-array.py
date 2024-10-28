class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = -1
        
        for num in nums:
            length = 0
            curr = num
            
            while curr in num_set:
                length += 1
                curr *= curr
                
            max_length = max(max_length, length)
        
        return max_length if max_length > 1 else -1