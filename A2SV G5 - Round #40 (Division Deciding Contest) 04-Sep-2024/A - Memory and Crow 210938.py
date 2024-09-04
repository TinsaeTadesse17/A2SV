# Problem: A - Memory and Crow - https://codeforces.com/gym/543431/problem/A

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[-1]]

for i in range(n-2,-1,-1):
    ans.append(arr[i+1] + arr[i])

print(*ans[::-1])
