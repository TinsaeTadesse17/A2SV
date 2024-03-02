class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        solutions = []
        
        # Sets to keep track of occupied rows, columns, and diagonals
        occupied_rows = set()
        occupied_columns = set()
        occupied_primary_diagonals = set()
        occupied_secondary_diagonals = set()
        
        def backtrack(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if (row not in occupied_rows and
                    col not in occupied_columns and
                    col - row not in occupied_primary_diagonals and
                    col + row not in occupied_secondary_diagonals):
                    
                    # Place queen
                    board[row][col] = "Q"
                    # Update occupied sets
                    occupied_rows.add(row)
                    occupied_columns.add(col)
                    occupied_primary_diagonals.add(col - row)
                    occupied_secondary_diagonals.add(col + row)
                    
                    # Move to the next row
                    backtrack(row + 1)
                    
                    # Remove queen and update occupied sets for backtracking
                    board[row][col] = "."
                    occupied_rows.remove(row)
                    occupied_columns.remove(col)
                    occupied_primary_diagonals.remove(col - row)
                    occupied_secondary_diagonals.remove(col + row)
        
        backtrack(0)
        return solutions
