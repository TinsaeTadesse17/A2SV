class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives , tens = 0 , 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if (fives < 1 or tens < 1) and fives < 3 :
                    return False
                else:
                    if tens >= 1:
                        fives -= 1
                        tens -= 1
                    else:
                        fives -= 3

        return True