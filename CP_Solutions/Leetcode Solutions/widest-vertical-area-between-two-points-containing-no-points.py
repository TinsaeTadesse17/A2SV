class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x = [i for i,j in points]

        x.sort()
        ans = 0

        for i in range(len(x)-1):
            if ans < x[i+1] - x[i]:
                ans = x[i+1] - x[i]  
        return ans