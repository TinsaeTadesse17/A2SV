class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n % 2:
            return x * pow(x * x , (n-1)//2)
        
        else:
            return pow(x * x , n//2)
            