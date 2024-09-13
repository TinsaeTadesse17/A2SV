# Problem: B - Fasika and Children - https://codeforces.com/gym/538762/problem/B

import math
n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_round = -1
ans = -1

for idx, num in enumerate(arr):
    rounds = math.ceil(num / m)
    if rounds >= max_round:
        max_round = rounds
        ans = idx

print(ans + 1)