class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        subboxdict = defaultdict(list)

        nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rowdict[i].append(int(board[i][j]))

        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    coldict[i].append(int(board[j][i]))

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    subboxdict[(i // 3, j // 3)].append(int(board[i][j]))

        for k in range(9):
            if len(set(rowdict[k])) == len(rowdict[k]) and set(rowdict[k]) <= nums:
                pass
            else:
                return False

            if len(set(coldict[k])) == len(coldict[k]) and set(coldict[k]) <= nums:
                pass
            else:
                return False

        for key in subboxdict:
            if len(set(subboxdict[key])) == len(subboxdict[key]) and set(subboxdict[key]) <= nums:
                pass
            else:
                return False

        return True