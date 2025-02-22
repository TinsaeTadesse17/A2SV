class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        m , n = len(matrix) , len(matrix[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1]) + 1

                    count += dp[i][j]

        return count