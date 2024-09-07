# Problem: B - Chore Partitioning - https://codeforces.com/gym/545013/problem/B

n , a , b = map(int, input().split())
complexity = list(map(int, input().split()))

complexity.sort()
ans = complexity[-a] - complexity[b-1]
if  ans > 0:
    print(ans)
else:
    print(0)