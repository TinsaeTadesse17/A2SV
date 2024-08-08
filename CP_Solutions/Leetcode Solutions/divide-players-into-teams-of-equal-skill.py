class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        target = skill[left] + skill[right]
        res = 0

        while left < right:
            
            if skill[left] + skill[right] != target:
                return -1

            else:
                res += skill[left] * skill[right]


            left += 1
            right -= 1

        return res

        

        

        
