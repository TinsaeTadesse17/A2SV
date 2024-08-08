class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        for i in range(len(nums)):
            ans[i] = nums[i] ** 2  
        ans.sort() 
        return ans
