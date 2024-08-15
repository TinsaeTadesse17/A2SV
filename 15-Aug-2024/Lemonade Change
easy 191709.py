# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_changes = 0
        ten_changes = 0
        n = len(bills)

        for i in range(n):
            if bills[i] == 10 and five_changes == 0:
                return False
            elif bills[i] == 20 and five_changes == 0 :
                return False

            elif bills[i] == 5:
                five_changes += 1
            elif bills[i] == 10:
                ten_changes += 1
                five_changes -= 1
            elif bills[i] == 20:
                if five_changes >= 1 and ten_changes >= 1:
                    ten_changes -= 1
                    five_changes -= 1
                elif ten_changes == 0 and five_changes >= 3:
                    five_changes -= 3
                elif ten_changes == 0 and five_changes < 3:
                    return False


        return True