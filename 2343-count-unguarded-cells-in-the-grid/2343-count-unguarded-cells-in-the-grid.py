class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def validate(row, col):
            return 0 <= row < m and 0 <= col < n

        grid = [[1] * n for _ in range(m)]

        # Convert guards and walls to sets for faster lookup
        guard_set = set(map(tuple, guards))
        wall_set = set(map(tuple, walls))

        # Mark guards and walls in the grid
        for row, col in guards:
            grid[row][col] = 0
        for row, col in walls:
            grid[row][col] = 0

        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row, col in guards:
            for dr, dc in directions:
                curr_row, curr_col = row + dr, col + dc
                while validate(curr_row, curr_col) and (curr_row, curr_col) not in wall_set and (curr_row, curr_col) not in guard_set:
                    grid[curr_row][curr_col] = 0
                    curr_row += dr
                    curr_col += dc

        return sum(cell for row in grid for cell in row)
