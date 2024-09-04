# Problem: B - Diversity - https://codeforces.com/gym/543431/problem/B

string = input()
k = int(input())

if len(set(string)) >= k:
    print(0)
elif len(string) < k:
    print("impossible")
else:
    print(k - len(set(string)))
