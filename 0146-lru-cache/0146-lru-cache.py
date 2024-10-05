class ListNode:
    def __init__(self,key=None,value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.addtoend(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.addtoend(node)
        else:
            if len(self.cache) == self.size:
                del_node = self.head.next
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next
                del self.cache[del_node.key]
            node = ListNode(key,value)
            self.addtoend(node)
            self.cache[key] = node

    def addtoend(self,node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)