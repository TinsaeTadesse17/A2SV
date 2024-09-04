# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    if n == 1:
        print(0)
    else:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            elif n % 3 == 0:
                n = (2 * n) // 3
                count += 1
            elif n % 5 == 0:
                n = (4 * n) // 5
                count += 1
            else:
                count = -1
                break
        print(count)