class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        mydict = nums.copy()
        ans = [0] * len(nums)
        nums.sort()

        for i in range(len(nums)):
            index = bisect_left(nums,mydict[i])

            ans[i] = index

        
        return ans