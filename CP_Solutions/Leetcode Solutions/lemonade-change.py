class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_changes = 0
        ten_changes = 0
        n = len(bills)

        for i in range(n):
            if bills[i] == 10:
                if five_changes == 0:
                    return False
                five_changes -= 1
                ten_changes += 1
            elif bills[i] == 20:
                if ten_changes > 0 and five_changes > 0:
                    ten_changes -= 1
                    five_changes -= 1
                elif five_changes >= 3:
                    five_changes -= 3
                else:
                    return False
            else:
                five_changes += 1

        return True
