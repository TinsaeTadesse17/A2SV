# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n > k:
        if n % k == 0:
            print(1)
        else:
            print(2)
    else:
        print(math.ceil(k/n))