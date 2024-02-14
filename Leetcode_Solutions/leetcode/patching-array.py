class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch_count = 0
        running_sum = 0
        i = 0

        while running_sum < n:
            if i < len(nums) and nums[i] <= running_sum + 1:
                running_sum += nums[i]
                i += 1
            else:
                running_sum += running_sum + 1
                patch_count += 1

        return patch_count
