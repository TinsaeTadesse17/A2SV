# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

from heapq import heapify, heappop, heappush

n = int(input())
m = int(input())
benches = []
for _ in range(n):
    benches.append(int(input()))
max_people = max(benches) + m
heapify(benches)
for i in range(m):
    min_bench = heappop(benches)
    heappush(benches, min_bench + 1)

print(max(benches),max_people)