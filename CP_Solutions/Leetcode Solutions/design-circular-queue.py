class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        self.size = 0
        self.front = 0
        self.rear = k - 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k