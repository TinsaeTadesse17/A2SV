class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums + nums
        m , n = len(nums) , len(arr)
        mon_stack = []

        for i in range(n-1,n//2-1,-1):
            while mon_stack and arr[i] >= mon_stack[-1]:
                mon_stack.pop()                
            mon_stack.append(arr[i])

        ans = [-1] * m
        for i in range(m-1,-1,-1):
            while mon_stack and arr[i] >= mon_stack[-1]:
                mon_stack.pop()
            if mon_stack:
                ans[i] = mon_stack[-1]
            mon_stack.append(arr[i])

        return ans
