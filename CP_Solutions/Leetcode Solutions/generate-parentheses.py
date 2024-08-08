class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        string = ["("]

        def backtrack(opening,closing):
            if len(string)==2*n:
                ans.append("".join(string))
                return

            if closing > opening:
                string.append(")")
                backtrack(opening,closing-1)
                string.pop()

            if opening:
                string.append("(")
                backtrack(opening-1,closing)
                string.pop()

        backtrack(n-1,n)
        return ans

