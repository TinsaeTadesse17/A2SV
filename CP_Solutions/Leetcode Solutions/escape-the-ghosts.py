class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_steps = abs(target[0]) + abs(target[1])
        ghost_steps = inf

        for i in ghosts:
            ghost_step = abs(target[0] - i[0]) + abs(target[1]-i[1])
            ghost_steps = min(ghost_step,ghost_steps)


        return my_steps < ghost_steps
          