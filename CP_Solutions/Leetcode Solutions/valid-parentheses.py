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
    def isValid(self, s: str) -> bool:
        stack = Stack()
        brackets_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.push(char)
            elif char in [')', '}', ']']:
                if stack.isEmpty():
                    return False
                top_char = stack.pop()
                if brackets_map[char] != top_char:
                    return False
        
        return stack.isEmpty()
