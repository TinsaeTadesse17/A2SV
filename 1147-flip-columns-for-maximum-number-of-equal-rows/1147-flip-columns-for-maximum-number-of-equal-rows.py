class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        half = 1 << (n - 1) 
        ones = (1 << n) - 1 

        nums = []
        for row in matrix:
          curr = 0
          for n in row:
            curr *= 2
            curr += n
          if curr < half:
            curr = curr ^ ones
          nums.append(curr)

        return max(Counter(nums).values())