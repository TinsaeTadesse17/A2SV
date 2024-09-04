# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

from collections import Counter
n = int(input())
for _ in range(n):
    s, t = input().split()
    counter = Counter(t)
    ptr1 = -1
    flag = True
    
    for i in range(len(s) - 1, -1, -1):
        if ptr1 >= -len(t) and s[i] == t[ptr1]:
            counter[t[ptr1]] -= 1
            ptr1 -= 1
            if ptr1 == -len(t)-1:
                break
        else:
            if s[i] in counter and counter[s[i]] > 0:
                flag = False
                break
    
    if ptr1 == -len(t)-1 and flag:
        print("YES")
    else:
        print("NO")