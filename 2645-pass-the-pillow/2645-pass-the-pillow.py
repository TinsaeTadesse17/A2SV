class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = n * 2 - 2  
        time = time % cycle_length 

        if time < n:
            return time + 1
        else:
            return n * 2 - time - 1
