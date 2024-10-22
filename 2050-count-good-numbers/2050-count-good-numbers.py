class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10 ** 9 + 7
        def binary_expo(a,b):
            if b == 0:
                return 1

            if b % 2 == 0:
                return binary_expo((a * a) % m , b//2)
            else:
                return a * binary_expo((a * a) % m , (b-1) // 2)

        if n % 2:
            return (binary_expo(5,ceil(n/2)) % m * binary_expo(4,n//2) % m) % m
        else:
            return (binary_expo(5,n/2) % m * binary_expo(4,n/2) % m) % m