class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self._add_to_end(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self._add_to_end(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_end(new_node)

    def _add_to_end(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
