class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = 0
        
        indices = []
        left  = 0
        right = 0
        max_score = float("-inf")

        for i in range(0, len(nums)+1):

            if i == 0:
                left  = 0
                right = sum(nums) 
            elif nums[i-1] == 0:
                left += 1
            else:
                right -= 1
            
            score = right + left

            if score > max_score:
                max_score = score
                indices = [i]
            elif score == max_score:
                indices.append(i)

        return indices