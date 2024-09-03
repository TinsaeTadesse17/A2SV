# Problem: A - Duale String - https://codeforces.com/gym/520688/problem/A

t = int(input())
for _ in range(t):
    string = input()
    n = len(string)
    if n % 2 != 0:
        print("NO")
    else:
        if string[:n//2] == string[n//2:]:
            print("YES")
        else:
            print("NO")