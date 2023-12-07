class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1 or (i > 0 and nums[i - 1] > nums[i + 1] and i < len(nums) - 2 and nums[i] > nums[i + 2]):
                    return False

        return True