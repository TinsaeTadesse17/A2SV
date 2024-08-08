class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        ans = []
        nums.sort(reverse=True)
        prefix_sum = [0] * (len(nums)+1)

        for i in range(1,len(nums)+1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i-1]

        for i in range(len(nums)):
            ans.append((nums[i] * (len(nums) - (i+1))) - (prefix_sum[-1] - prefix_sum[i+1]) + abs(nums[i] * i - prefix_sum[i]))
        
        ans.reverse()
        return ans

        

        



        
