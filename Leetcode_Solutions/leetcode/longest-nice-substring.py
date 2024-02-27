class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        distinctChars = set(s)

        for i,string in enumerate(s):
            if string.swapcase() not in distinctChars:
                left =  self.longestNiceSubstring(s[0:i])
                right = self.longestNiceSubstring(s[i+1:])

                return left if len(left) >= len(right) else right

        return s


        

    