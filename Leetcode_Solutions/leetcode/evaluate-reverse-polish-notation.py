class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.val  
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.val

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        operand1 = 0
        operand2 = 0
        
        for token in tokens:
            
            if token == '+':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push(int(operand1) + int(operand2))
            elif token == '-':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push(int(operand1) - int(operand2))
            elif token == '*':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push(int(operand1) * int(operand2))
            elif token == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push(int(operand1) / int(operand2))
            else:
                stack.push(int(token))
        return int(stack.peek())
