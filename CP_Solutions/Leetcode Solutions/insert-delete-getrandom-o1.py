class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()

    def insert(self, val: int) -> bool:
        if val not in self.randomizedSet:
            self.randomizedSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomizedSet))