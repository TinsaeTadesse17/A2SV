class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        ans =  [[],[]]

        from collections import defaultdict
        
        winner = defaultdict(int)
        loser = defaultdict(int)

        for i in matches:

            winner[i[0]] += 1
            loser[i[1]] +=1
        
        for j in winner.keys():
            if j not in loser.keys():
                ans[0].append(j)

        for k in loser.keys():
            if loser[k] == 1:
                ans[1].append(k)
        ans[0].sort()
        ans[1].sort()

        return ans

