# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n , m , k = map(int,input().split())
players = []
friends = 0
for _ in range(m+1):
    x = int(input())
    players.append(x)
for i in range(len(players)-2,-1,-1):
    xor = players[-1] ^ players[i]
    if bin(xor).count('1') <= k:
        friends += 1
print(friends)
    
