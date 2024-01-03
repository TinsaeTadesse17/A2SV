class Solution:
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        ans = 0
        i, j = 0, len(piles) - 1

        while i < j:
            i += 1  
            ans += piles[i]  
            i += 1
            j -= 1  

        return ans
