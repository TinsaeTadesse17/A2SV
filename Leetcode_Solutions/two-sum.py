from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        num = [(numm, index) for index, numm in enumerate(nums)]

       
        num.sort(key=lambda x: x[0])

        i = 0
        j = len(nums) - 1

        while i < j:
            curr = num[i][0] + num[j][0]

            if curr > target:
                j -= 1
            elif curr < target:
                i += 1
            else:
               
                return [num[i][1], num[j][1]]


