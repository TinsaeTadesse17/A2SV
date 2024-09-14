# Problem: A - Shalamagando's  workout - https://codeforces.com/gym/517685/problem/A

n = int(input())
arr = list(map(int, input().split()))
ans = [0,0,0]
for i in range(n):
    ans[i%3] += arr[i]

if ans[0] == max(ans):
    print("chest")
elif ans[1] == max(ans):
    print("biceps")
else:    
    print("back")