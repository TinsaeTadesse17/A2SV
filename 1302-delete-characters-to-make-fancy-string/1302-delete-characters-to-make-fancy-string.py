class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        ans = ""
        count = 1  

        for i in range(n):
            if count <= 2:
                ans += s[i]
            
            if i < n - 1 and s[i] == s[i + 1]:
                count += 1 
            else:
                count = 1  

        return ans
