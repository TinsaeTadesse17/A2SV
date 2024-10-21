# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    flag = True
    if n % 7 == 0:
        print(n)
        flag = False
    if flag:
       

        for i in range(10):
            num = str(n)[:-1]
            num = num + str(i)
            if int(num )% 7 == 0:
                print(int(num))
                break