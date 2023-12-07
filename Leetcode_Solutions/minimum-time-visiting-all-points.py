class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            x_diff = abs(points[i+1][0] - points[i][0])
            y_diff = abs(points[i+1][1] - points[i][1])
            
            time += max(x_diff, y_diff)
        
        return int(time)