class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Calculate prefix sums
        prefix_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix_sums[r][c] += prefix_sums[r][c - 1] + matrix[r - 1][c - 1]

        count = 0

        # Iterate over all possible submatrices
        for left in range(cols):
            for right in range(left + 1, cols + 1):
                frequency = defaultdict(int)
                total_sum = 0

                # Slide through rows to calculate submatrix sum
                for row in range(rows + 1):
                    total_sum += prefix_sums[row][right] - prefix_sums[row][left]
                    # If there is a submatrix with sum equal to target
                    count += frequency[total_sum - target]
                    frequency[total_sum] += 1

        return count
