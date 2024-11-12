class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in "+-/*":
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()

                if char =="+":
                    stack.append(int(operand1) + int(operand2))
                elif char =="-":
                    stack.append(int(operand2) - int(operand1))
                elif char =="*":
                    stack.append(int(operand1) * int(operand2))
                else:
                    stack.append(int(operand2) / int(operand1))

        return int(stack[0])
