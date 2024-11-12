class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack and char in ")}]":
                    return False
                elif stack[-1] == "(" and char == ")":
                    stack.pop()
                elif stack[-1] == "{" and char == "}":
                    stack.pop()
                elif stack[-1] == "[" and char == "]":
                    stack.pop()
                else:
                    return False
        return not stack