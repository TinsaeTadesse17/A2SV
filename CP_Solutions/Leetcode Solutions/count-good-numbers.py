class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        
        def myPow(x,n):

            if n==0:
                return 1
            
            if n%2==0:
                return myPow((x*x)%mod, n//2)
            else:
                return x * myPow((x*x)%mod, (n-1)//2)




        if n % 2 == 0:
            return (myPow(4,n //2) % mod * myPow(5,n//2) % mod ) % mod
        else:
            return (myPow(5,ceil(n/2)) % mod * myPow(4,n//2) % mod)  % mod

