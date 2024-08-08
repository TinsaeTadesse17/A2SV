class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row, col, k):
            
            for i in range(9):             
                if board[i][col] == k:
                    return False
                if board[row][i] == k:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == k:
                    return False
            return True    

        def backtrack(row, col):
            
            if row == 9:
                return True
            if col == 9:
                return backtrack(row + 1, 0)    
            if board[row][col] == '.':
                for k in range(1, 10):
                    if is_valid(row, col, str(k)):
                        board[row][col] = str(k)
                        if backtrack(row, col + 1):
                            return True
                        board[row][col] = '.'
                return False
            return backtrack(row, col + 1)        

        # Start backtracking from the top-left corner
        backtrack(0, 0)
