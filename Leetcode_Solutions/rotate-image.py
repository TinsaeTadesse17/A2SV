class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j=0
        k=len(matrix[0])-1

        for i in range(len(matrix)):

            for j in range(i,len(matrix[0])):

                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] 

            matrix[i].reverse()

        return matrix


    