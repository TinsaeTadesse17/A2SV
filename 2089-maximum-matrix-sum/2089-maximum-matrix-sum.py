class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        nums = min((num for row in matrix for num in row), key=abs)
        s = 0
        for i in matrix:
            for j in i:
                if j < 0:
                    neg += 1
                s += abs(j)
        if neg % 2 == 0:
            return(s)
        else:
            return(s - abs(nums * 2))

        