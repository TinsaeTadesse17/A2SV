class AllOne:

    def __init__(self):
        self.hashmap = {}

    def inc(self, key: str) -> None:
        if key in self.hashmap:
            self.hashmap[key] += 1
        else:
            self.hashmap[key] =  1
        return None
        
    def dec(self, key: str) -> None:
        if self.hashmap[key] > 1:      
            self.hashmap[key] -= 1
        else:
            self.hashmap.pop(key)
        return None
    def getMaxKey(self) -> str:
        if not self.hashmap:
            return ""
        return max(self.hashmap, key=self.hashmap.get)

    def getMinKey(self) -> str:
        if not self.hashmap:
            return ""
        return min(self.hashmap, key=self.hashmap.get)
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()