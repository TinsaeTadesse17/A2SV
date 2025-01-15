class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                s += i 
                s += num / i 
        if num == s:
            return True
        return False