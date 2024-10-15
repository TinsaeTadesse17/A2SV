class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        n = len(temperatures)
        
        for i in range(n-1 ,-1, -1):
            if stack:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1][1] - i
            stack.append((temperatures[i],i))
            
        return ans


