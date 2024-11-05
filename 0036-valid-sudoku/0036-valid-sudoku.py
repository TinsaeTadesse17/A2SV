class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False

        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in col:
                        col.add(board[i][j])
                    else:
                        return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                subbox = set()
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y] != ".":
                            if board[x][y] not in subbox:
                                subbox.add(board[x][y])
                            else:
                                return False

        return True

