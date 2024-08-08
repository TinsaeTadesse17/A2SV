class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:

            seen.add(n)
            sum = 0

            while n > 0:
                sum += (n % 10) * (n % 10)
                n = floor(n/10)

            if sum == 1:
                return True

            n = sum
            
        return False 