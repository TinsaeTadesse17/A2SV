class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  
        dir_idx = 0  
        max_dist = 0
        
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # turn left
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # move forward
                for _ in range(command):
                    nx = x + directions[dir_idx][0]
                    ny = y + directions[dir_idx][1]
                    
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_dist = max(max_dist, x * x + y * y)
                    else:
                        break  #obstacle
        
        return max_dist