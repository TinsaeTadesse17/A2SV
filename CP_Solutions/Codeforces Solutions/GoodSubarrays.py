from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    
    numbers = input()

    prefix_sums = []
    current_sum = 0

    for i in range(n):
        current_sum += int(numbers[i])
        prefix_sums.append(current_sum)

    count = 0
    visited_sums = defaultdict(int)
    visited_sums[0] = 1

    for j in range(len(prefix_sums)):
        current_pair_value = prefix_sums[j] - j - 1

        if current_pair_value in visited_sums:
            count += visited_sums[current_pair_value]
        
        visited_sums[current_pair_value] += 1

    print(count)