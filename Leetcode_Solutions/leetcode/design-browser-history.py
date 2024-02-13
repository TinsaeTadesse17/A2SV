class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.length = 1  
        self.forwardLength = 0  

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node
        self.length += 1
        self.forwardLength = 0  

    def back(self, steps: int) -> str:
        for _ in range(min(steps, self.length - 1)):  
            if self.curr.prev:  
                self.curr = self.curr.prev
                self.forwardLength += 1
        return self.curr.value

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, self.forwardLength)): 
            if self.curr.next:  
                self.curr = self.curr.next
        return self.curr.value
