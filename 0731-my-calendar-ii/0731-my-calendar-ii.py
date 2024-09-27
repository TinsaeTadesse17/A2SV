class MyCalendarTwo:

    def __init__(self):
        self.singlebooking = []
        self.doublebooking = []

    def book(self, start: int, end: int) -> bool:
        for s , e in self.doublebooking:
            if start < e and end > s:
                return False

        for s , e in self.singlebooking:
            if start < e and end > s:
                self.doublebooking.append((max(start,s) , min(end , e)))

        self.singlebooking.append((start,end))
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)