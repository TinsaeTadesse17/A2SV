# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

import math
t = int(input())
for _ in range(t):
    n = int(input())
    print(math.ceil(n / 2 ))
    start , end = 1 , 3 * n
    while start < end:
        print(start,end)
        start += 3
        end -= 3

        
