class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows , cols = len(grid2) , len(grid2[0])
        visited = set()

        def checker(row,col):
            if row < 0 or col < 0 or row == rows or col == cols or (row,col) in visited or grid2[row][col] == 0:
                return True


        def dfs(row,col):
            if checker(row,col):
                return True
            #checker didn't return True & this renders, it means (row,col) not visited
            visited.add((row,col)) 

            ans = True
            if grid1[row][col] == 0:
                ans = False

            ans = dfs(row+1,col) and ans
            ans = dfs(row-1,col) and ans
            ans = dfs(row,col+1) and ans
            ans = dfs(row,col-1) and ans

            return ans


        subislands = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and (row,col) not in visited and dfs(row,col):
                    subislands += 1

        return subislands
