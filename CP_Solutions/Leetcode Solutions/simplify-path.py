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
    def simplifyPath(self, path: str) -> str:
        stack = Stack()

        # Split the path by '/'
        for directory in path.split('/'):
            if directory in ('', '.'):
                # Skip empty directories or current directory '.'
                continue
            elif directory == '..':
                # Go back one directory if possible
                if not stack.isEmpty():
                    stack.pop()
            else:
                # Push valid directory names onto the stack
                stack.push(directory)

        # Build the result string from the stack
        result = []
        while not stack.isEmpty():
            result.append(stack.pop())

        # If the result is empty, return the root directory '/'
        return '/' + '/'.join(result[::-1]) if result else '/'


        