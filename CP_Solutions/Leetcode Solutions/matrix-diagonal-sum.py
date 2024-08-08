class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        primarysum = 0
        secondarysum = 0
        
        for i in range(n):
            for  j in range(n):
                if i == j:
                    primarysum += mat[i][j]

                if i + j == n-1 and i != j:
                    secondarysum += mat[i][j]

        return primarysum + secondarysum

        
                
