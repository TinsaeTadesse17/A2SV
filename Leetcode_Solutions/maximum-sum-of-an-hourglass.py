class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        maxsum = 0

        while i + 2 < len(grid):
            while j + 2 < len(grid[0]):
                current_sum = (
                    grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]  
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2]
                )
                maxsum = max(maxsum, current_sum)
                j += 1

            
            j = 0
            i += 1

        return maxsum