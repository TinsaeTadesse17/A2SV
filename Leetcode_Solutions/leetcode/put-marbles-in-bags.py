class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # create an array of weights.length-1
        pairCosts = [0] * (len(weights)-1)
        
        # store all the possible Pairs sum
        for i in range(len(weights) - 1):
            pairCosts[i] = weights[i] + weights[i + 1]

        # ascending order sorting
        pairCosts.sort()

        ans = 0
        # get the sum for all pairs differences
        for i in range(k - 1):
            ans += pairCosts[len(pairCosts) - 1 - i] - pairCosts[i]

        return ans