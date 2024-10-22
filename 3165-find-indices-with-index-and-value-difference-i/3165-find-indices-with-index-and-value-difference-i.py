class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1 , -1]
        i , j = 0 , len(nums) - 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(j - i) >= indexDifference and abs(nums[j] - nums[i]) >= valueDifference:
                    ans = [i , j]
                    break

        return ans
