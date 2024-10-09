class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        forwardBrace = 0
        backwardBrace = 0
        
        for parenthesis  in s:
            if parenthesis == "(":
                forwardBrace += 1
            else:
                if forwardBrace > 0:
                    forwardBrace -= 1
                else:
                    backwardBrace += 1

        return forwardBrace + backwardBrace