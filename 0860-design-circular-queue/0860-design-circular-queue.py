class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [] * self.size
        self.length = 0
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            self.length += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            self.length -= 1  
            return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]
    
    def isEmpty(self) -> bool:
        return self.length == 0
        
    def isFull(self) -> bool:
        return self.length == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()