class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 0

                while current_num in nums_set:
                    current_num += 1
                    current_length += 1

                longest_sequence = max(longest_sequence, current_length)

        return longest_sequence
