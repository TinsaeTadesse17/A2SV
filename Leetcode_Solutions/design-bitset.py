class Bitset:
    def __init__(self, size: int):
        self.bitset = ['0'] * size  
        self.flipbit = ['1'] * size 
        self.counts = 0

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == '0':
            self.counts += 1
        self.bitset[idx] = '1'
        self.flipbit[idx] = '0'

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == '1':
            self.counts -= 1
        self.bitset[idx] = '0'
        self.flipbit[idx] = '1'

    def flip(self) -> None:
        self.bitset, self.flipbit = self.flipbit, self.bitset
        self.counts = len(self.bitset) - self.counts

    def all(self) -> bool:
        return self.counts == len(self.bitset)

    def one(self) -> bool:
        return self.counts

    def count(self) -> int:
        return self.counts

    def toString(self) -> str:
        return ''.join(self.bitset)



        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()