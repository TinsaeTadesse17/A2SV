# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        right = n - 1
        down = m - 1
        total = right + down

        return factorial(total) // (factorial(right) * factorial(down))