class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        idx = 1
        num = 1
    
        while num <= n-1:
            if idx & x==0:
                if num & (n-1):
                    res = res | idx
                num = num << 1
            idx = idx << 1

        return res