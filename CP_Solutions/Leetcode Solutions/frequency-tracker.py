class FrequencyTracker :

    def __init__(self):
        self.freq = defaultdict(int)
        self.counter = defaultdict(int)
        

    def add(self, number: int) -> None:

        self.freq[number] += 1
        self.counter[self.freq[number]] += 1


        if self.freq[number]-1 in self.counter:
            self.counter[self.freq[number]-1] -= 1
            if self.counter[self.freq[number]-1] == 0:
                del self.counter[self.freq[number]-1]


    def deleteOne(self, number: int) -> None:

        if number in self.freq:

            if self.counter[self.freq[number]] == 0:
                del self.counter[self.freq[number]]

            self.counter[self.freq[number]] -= 1

            self.freq[number] -= 1

            self.counter[self.freq[number]] += 1

            if self.freq[number] == 0:
                del self.freq[number]

              

    def hasFrequency(self, frequency: int) -> bool:
        
        if frequency in self.counter and self.counter[frequency] != 0:
            return True

        else:
            return False
            
    

# Your freq object will be instantiated and called as such:
# obj = freq()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)