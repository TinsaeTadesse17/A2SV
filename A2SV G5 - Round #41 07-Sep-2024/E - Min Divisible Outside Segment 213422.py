# Problem: E - Min Divisible Outside Segment - https://codeforces.com/gym/545013/problem/E

t = int(input())

for _ in range(t):

    l , r , d = map(int,input().split())
    if l <= d <= r:
        ans = ((r // d) + 1) * d
    elif d < l:
        ans = d
    else:
        ans = d

    print(ans)
