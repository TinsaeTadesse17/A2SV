class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n , ans = len(skill) , 0
        skill.sort()
        team_sum = sum(skill) / (n/2)
        
        i , j = 0 , n-1
        while i < j:
            if skill[i] + skill[j] == team_sum:
                ans += skill[i] * skill[j]
                i += 1
                j -= 1
            else:
                ans = -1
                break
        return ans


