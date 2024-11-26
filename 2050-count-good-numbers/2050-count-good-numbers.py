class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def modular_expo(base,exp,m):
            res = 1
            while exp > 0:
                if exp & 1 :
                    res = (res * base) % m
                base = (base * base) % m
                exp >>= 1
            return res

        m = 10 ** 9 + 7
        even_pos = ceil(n/2)
        odd_pos = n // 2

        return  (modular_expo(5 , even_pos,m) * modular_expo(4 , odd_pos , m)) % m

