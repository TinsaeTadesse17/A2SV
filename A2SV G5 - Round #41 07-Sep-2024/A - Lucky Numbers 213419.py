# Problem: A - Lucky Numbers - https://codeforces.com/gym/545013/problem/A

n,k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
ans = 0

for i in range(n):
    for j in str(arr[i]):
        if j == "4" or j == "7":
            count += 1
    if count <= k:
        ans += 1
    count = 0

print(ans)