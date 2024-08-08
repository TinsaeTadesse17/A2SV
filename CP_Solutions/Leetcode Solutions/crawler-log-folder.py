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
            

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = Stack()

        for log in logs: 
            if log == "../":
                stack.pop()
            elif log == "./":
                continue
            else:
                stack.push(log)
            
        return stack.length

        