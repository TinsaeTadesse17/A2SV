# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        uniqueSearch = 1
        n = len(nums)

        while uniqueSearch < n:
            if nums[uniqueSearch] != nums[unique]:
                nums[unique + 1] = nums[uniqueSearch]
                unique += 1
                uniqueSearch += 1
            else:
                uniqueSearch += 1

        return unique + 1