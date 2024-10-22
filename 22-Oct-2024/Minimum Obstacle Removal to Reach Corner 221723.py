# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        obs_count = [[float("inf") for _ in range(n)] for _ in range(m)]
        obs_count[0][0] = 0

        heap = [(0 , 0, 0)]
        while heap:
            obs , row , col = heapq.heappop(heap)

            if row == m - 1 and col == n-1 :
                return obs

            for new_row , new_col in [(row + 1, col) , (row - 1, col) , (row, col+1), (row, col - 1)]:
                if 0 <= new_row < m and 0 <= new_col < n:

                    if obs_count[new_row][new_col] > obs + grid[new_row][new_col] :
                        obs_count[new_row][new_col] = obs + grid[new_row][new_col]
                        heapq.heappush(heap , (obs + grid[new_row][new_col],new_row,new_col))

        return -1

                    
                    
                
