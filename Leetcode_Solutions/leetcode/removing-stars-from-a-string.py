class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.val  

class Solution:
    def removeStars(self, s: str) -> str:
        stack = Stack()
        for char in s:
            stack.push(char)
            if char == "*":
                stack.pop()
                stack.pop()

        result = ""
        while not stack.isEmpty():
            result += stack.pop()
        return result[::-1]
        