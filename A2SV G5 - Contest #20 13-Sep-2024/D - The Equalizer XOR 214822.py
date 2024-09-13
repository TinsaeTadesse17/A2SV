# Problem: D - The Equalizer XOR - https://codeforces.com/gym/528792/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True

    total_xor = 0
    for num in arr:
        total_xor ^= num
    
    # can make all elt equal if total_xor is 0
    if total_xor == 0:
        print("YES")
        flag = False
    
    # try partitioning arr into at least two parts with equal XOR
    prefix_xor = 0
    partitions = 0
    
    for num in arr:
        prefix_xor ^= num
        if prefix_xor == total_xor:
            partitions += 1
            prefix_xor = 0  # next partition
    
    if flag:
        if partitions >= 2:
            print("YES")
        else:
            print("NO")

