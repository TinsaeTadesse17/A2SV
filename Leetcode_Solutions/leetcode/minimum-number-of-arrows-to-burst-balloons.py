class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        start = points[0][0]
        end = points[0][1]
        points = points[1:]

        for i,j in points:
            if i not in range(start,end + 1):
                arrow += 1
                start = i
                end = j
            else:
                start = max(i,start)
                end = min(j,end)

        return arrow
        