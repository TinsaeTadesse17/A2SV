class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ")":
                temp = stack.pop()
                if temp == "(":
                    stack.append(1)
                else:
                    curr = temp
                    while stack[-1] != "(":
                        curr += stack.pop()
                    stack.pop()
                    stack.append( 2 * curr)
            else:
                stack.append(char)

        return sum(stack)