class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left_monstack = []
        left = [-1] * n
        for i in range(n):
            while left_monstack and arr[i] <= arr[left_monstack[-1]]: # if this is less or equal, the right stack needs to be less only, to account for the duplicates and avoid counting twice, they need to be included on the right or the left but not both
                left_monstack.pop()
            if left_monstack:
                left[i] = left_monstack[-1]
            else:
                left[i] = -1
            left_monstack.append(i)
            

        right_monstack = []
        right = [n] * n
        for i in range(n-1,-1,-1):
            while right_monstack  and arr[i] < arr[right_monstack [-1]]:
                right_monstack.pop()
            if right_monstack:
                right[i] = right_monstack[-1]
            else:
                right[i] = n
            right_monstack.append(i)

        ans = 0
        for i in range(n):
            ans += ((i - left[i]) * (right[i] - i)) * arr[i]

        return ans % (10**9 + 7)

