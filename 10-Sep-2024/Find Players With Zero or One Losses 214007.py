# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners , loser_count = set() , Counter()
        
        for winner, loser in matches:
            winners.add(winner)
            loser_count[loser] += 1

        champs = [winner for winner in winners if winner not in loser_count]
        almost_champs = [player for player in loser_count if loser_count[player] == 1]

        champs.sort()
        almost_champs.sort()

        return [champs,almost_champs]


