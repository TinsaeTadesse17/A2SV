class OrderedStream:

    def __init__(self, n: int):
        self.idKey = 0
        self.values = [""] * n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.values[idKey] = value

        if idKey > self.idKey: 
            return []

        while self.idKey < len(self.values) and self.values[self.idKey]:
            self.idKey +=1

        return self.values[idKey:self.idKey]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)