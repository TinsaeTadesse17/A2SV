# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import Counter
from math import gcd

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = Counter()
zeros = 0

for i in range(n):
    if arr1[i] == 0 and arr2[i] == 0:
        zeros += 1
    elif arr1[i] == 0:
        continue
    elif arr2[i] == 0:
        count[(0, 1)] += 1
    else:
        g = gcd(arr1[i], arr2[i])
        a, b = arr2[i] // g, arr1[i] // g
        if b < 0:
            a, b = -a, -b
        count[(a, b)] += 1

max_count = max(count.values(), default=0)

ans = max_count + zeros
print(ans)