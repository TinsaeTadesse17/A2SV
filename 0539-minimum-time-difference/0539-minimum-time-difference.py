class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        def converter(time):
            hours , minutes = map(int,time.split(":"))
            return 60 * hours + minutes

        minutes = [converter(time) for time in timePoints]
        #1440 is minutes in a day
        #considering circular time diff b/n the first and the last time points  
        ans = 1440 - converter(timePoints[-1]) + converter(timePoints[0])

        for i in range(1,len(timePoints)):
            diff = converter(timePoints[i]) - converter(timePoints[i-1])
            ans = min(ans,diff)

        return ans

