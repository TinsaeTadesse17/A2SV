class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        columnSkyLine = []
        rowSkyLine = []
        finalSum = 0
        initialSum = 0
        
        for j in range(len(grid[0])):
            skyLine = 0
            for i in range(len(grid)):
                skyLine = max(skyLine,grid[i][j])
            columnSkyLine.append(skyLine)

        for i in range(len(grid)):
            skyLine = 0
            for j in range(len(grid[0])):
                skyLine = max(skyLine,grid[i][j])
            rowSkyLine.append(skyLine)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                finalSum += min(rowSkyLine[i],columnSkyLine[j])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                initialSum += grid[i][j]
    

        return  finalSum - initialSum

        

