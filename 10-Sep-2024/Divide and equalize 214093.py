# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import Counter
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    factorization = []
    for num in arr:
        d = 2
        while d * d <= num:
            while num % d == 0:
                factorization.append(d)
                num //= d
            d += 1
        if num > 1:
            factorization.append(num)

    counter = Counter(factorization)
    flag = True
    for count in counter.values():
        if count % len(arr) != 0:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")
    
       


  