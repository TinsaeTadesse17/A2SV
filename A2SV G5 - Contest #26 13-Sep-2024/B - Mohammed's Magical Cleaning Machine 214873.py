# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    count_zero = 0
    dust_level = 0
    flag = False

    for i in range(len(arr)-1):
        if arr[i] != 0:
            dust_level += arr[i]
            flag = True
        if flag and arr[i] == 0:
            count_zero += 1

    print(count_zero + dust_level)
