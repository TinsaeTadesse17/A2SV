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
    def scoreOfParentheses(self, s: str) -> int:
        stack = Stack()
        temp = 0
        ans = 0
        for par in s:
            if par == "(":
                stack.push(par)
            else:
                if stack.peek() == "(":
                    stack.pop()
                    temp = 1
                else:
                    while stack.peek() != "(":
                        temp += stack.pop()
                    stack.pop()
                    temp = temp * 2

                stack.push(temp)
                temp = 0

        while stack.length != 0:
            ans += stack.pop()
        return ans