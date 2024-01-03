class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev_idx = 0
        for i in range (0,len(nums)):
            if nums[i] != 0 :
                temp = nums[prev_idx]
                nums[prev_idx] = nums[i]
                nums[i] = temp
                prev_idx += 1