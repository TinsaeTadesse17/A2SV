# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            # max possible(worst case) value for dp[i], paste 1 'A' i-1 times
            dp[i] = i  
            
            #find factors of i
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        
        return dp[n]
