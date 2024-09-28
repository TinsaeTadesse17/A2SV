class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.deque = [0] * k
        self.front = 0
        self.back = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.front = (self.front - 1 + self.k) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.back = (self.back + 1) % self.k
        self.deque[self.back] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.back = (self.back - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[self.back]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k