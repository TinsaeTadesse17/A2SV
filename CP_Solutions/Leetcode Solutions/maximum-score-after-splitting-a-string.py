class Solution:
    def maxScore(self, s: str) -> int:

        s =list(map(int,s))
        tot_sum = sum(s)
        prefix_sum,score = 0,0

        for i in range(len(s)-1):
            prefix_sum += s[i]
            score = max(score , i + 1 - prefix_sum + tot_sum - prefix_sum)

        return score
            