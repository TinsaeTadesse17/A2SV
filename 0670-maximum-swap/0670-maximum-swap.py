class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        for i, a in enumerate(arr):
            arr[i] = int(a)

        arr.sort(reverse=True)
        num = list(str(num))
        n = len(num)

        swap = float("inf")
        swap_idx = -1

        for idx, digit in enumerate(num):
            if digit != str(arr[idx]):
                swap = str(arr[idx])
                swap_idx = idx
                break

        if swap != float("inf"):
            for i in range(n-1, -1, -1):
                if num[i] == swap:
                    num[i] , num[swap_idx] = num[swap_idx] , num[i]

        return int(''.join(num))