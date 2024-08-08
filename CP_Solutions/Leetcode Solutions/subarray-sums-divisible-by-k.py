class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum, count = 0 , 0
        my_dict = {0:1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum % k in my_dict:
                count += my_dict[prefix_sum % k]
            my_dict[prefix_sum % k] = my_dict.get(prefix_sum % k , 0) + 1

        return count
