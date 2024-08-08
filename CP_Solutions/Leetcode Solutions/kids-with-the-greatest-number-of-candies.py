from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for num_candies in candies:
            if num_candies + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
