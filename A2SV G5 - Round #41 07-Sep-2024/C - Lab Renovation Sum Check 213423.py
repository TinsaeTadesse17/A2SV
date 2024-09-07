# Problem: C - Lab Renovation Sum Check - https://codeforces.com/gym/545013/problem/C

n = int(input())  

lab = [] 
for _ in range(n):
    row = list(map(int, input().split())) 
    lab.append(row)

is_good = True 

for i in range(n):
    for j in range(n):
        if lab[i][j] != 1:  
            flag = False
            for k in range(n):
                for l in range(n):
                    if lab[i][j] == lab[i][k] + lab[l][j]:
                        flag = True
                        break  
                if flag:
                    break
            if not flag:
                is_good = False  
                break  
    if not is_good:
        break

if is_good:
    print("Yes")
else:
    print("No")