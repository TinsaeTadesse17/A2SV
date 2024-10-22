class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10 ** 9 + 7

        diff = endPos - startPos
        a = (k - diff) // 2
        b = a + diff

        if a < 0  or b < 0 or (k - diff) % 2:
            return 0
        elif diff == 0:
            return factorial(k) // (factorial(k//2)* factorial(k//2)) % mod
        else:
            return factorial(k) // (factorial(a)* factorial(b)) % mod



