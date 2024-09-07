# Problem: D - Card Dealing - https://codeforces.com/gym/545013/problem/D

t = int(input())

for _ in range(t):
    cards = int(input()) - 1

    alice = 1
    bob = 0
    card = 2

    while cards > 0:
        if cards >= 2 * card + 1:
            bob += 2 * card + 1
            cards -= 2 * card + 1
        else:
            bob += cards
            cards = 0

        if cards == 0:
            break
        card += 2
        if cards >= 2 * card + 1:
            alice += 2 * card + 1
            cards -= 2 * card + 1
            card += 2
        else:
            alice += cards 
            cards = 0
    print(alice,bob)