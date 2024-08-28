class Solution:
    def nthUglyNumber(self, n: int) -> int:
 
        ugly = [0] * n
        ugly[0] = 1  # The first ugly number is always 1
        
        p2, p3, p5 = 0, 0, 0
        
        # Initial multiples of 2, 3, and 5
        next2, next3, next5 = 2, 3, 5
        
        for i in range(1, n):
            # The next ugly number is the minimum of the multiples of 2, 3, and 5
            ugly[i] = min(next2, next3, next5)
            
            # Move pointers that produced the next ugly number
            if ugly[i] == next2:
                p2 += 1
                next2 = ugly[p2] * 2
            
            if ugly[i] == next3:
                p3 += 1
                next3 = ugly[p3] * 3
            
            if ugly[i] == next5:
                p5 += 1
                next5 = ugly[p5] * 5
        
        return ugly[-1]
