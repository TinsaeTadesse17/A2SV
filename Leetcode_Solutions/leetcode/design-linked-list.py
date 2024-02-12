class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = Node(None)

    def get(self, index: int) -> int:
        idx = -1
        curr = self.head

        while curr:
            if idx == index:
                return curr.value
            curr = curr.next
            idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        idx = -1
        curr = self.head
        while curr.next:
            if idx + 1 == index:
                curr.next = curr.next.next
                break
            curr = curr.next
            idx += 1
        self.length -= 1
