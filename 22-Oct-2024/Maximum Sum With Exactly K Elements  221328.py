# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        num = max(nums)

        for _ in range(k):
            score += num
            num += 1
            
        return score

