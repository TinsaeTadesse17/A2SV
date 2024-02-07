class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):

            if i == 0:
                prefix[i] = 0 + nums[i]
            else:
                prefix[i] = prefix[i-1] + nums[i]

            if prefix[i] - nums[i] == sum(nums) - prefix[i]:
                return i
        else:
            return -1
        

            