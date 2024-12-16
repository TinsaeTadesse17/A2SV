class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            curr = min(nums)
            idx = nums.index(curr)
            nums[idx] = curr * multiplier
        return nums