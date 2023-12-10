class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_dict = {num: i for i, num in enumerate(nums)}

        for operation in operations:
            num_to_replace, new_value = operation
            if num_to_replace in index_dict:
                index = index_dict[num_to_replace]
                nums[index] = new_value
                index_dict[new_value] = index
                del index_dict[num_to_replace]

        return nums