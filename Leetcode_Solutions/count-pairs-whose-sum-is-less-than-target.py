class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
           
                if nums[i]  + nums[j] >= target:
                    j -= 1
                elif nums[i]  + nums[j] < target:
                    count += j-i
                    i += 1

                
        
        return count
