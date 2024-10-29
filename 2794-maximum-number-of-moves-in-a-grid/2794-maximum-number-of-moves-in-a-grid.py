class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            res = 0 
            cur = grid[i][j]
            for x, y in [(-1, 1), (0, 1), (1, 1)]:
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] > cur:
                    res = max(res, dp(i + x, j + y) + 1)
            return res
        ans = 0
        for i in range(m):
            ans = max(ans, dp(i, 0))
        return ans