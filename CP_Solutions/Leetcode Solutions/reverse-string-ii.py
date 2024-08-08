import math

class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s) < k:
            s[::-1]

        s = list(s)

        for i in range(0,len(s), 2*k):
            s[i:i+k] = (s[i:i+k]) [::-1]
            
        return ''.join(s)