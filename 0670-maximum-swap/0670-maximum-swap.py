class Solution:
    def maximumSwap(self, num: int) -> int:

        '''if we have the digit with its index in a hashmap, when we iterate through 
        the number's digit, we can check if a greater number than the digit exists 
        in a hashmap(iterating through 9 upto the digit), if so, we need to swap it 
        to get greater number'''

        arr = list(str(num))
        hashmap = {int(digit):idx for idx, digit in enumerate(arr)}

        for i, d in enumerate(arr):
            for digit in range(9, int(d), -1):
                if hashmap.get(digit,-1) > i:
                    arr[i] , arr[hashmap[digit]] = arr[hashmap[digit]] , arr[i]
                    return int(''.join(arr))

        return num
        