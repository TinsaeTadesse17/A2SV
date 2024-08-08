class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt = [num for num in nums if num < pivot]
        eq = [num for num in nums if num == pivot]
        gt = [num for num in nums if num > pivot]

        return lt + eq + gt