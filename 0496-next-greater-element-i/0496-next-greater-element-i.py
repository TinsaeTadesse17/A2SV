class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        mon_stack = []
        nxt_greater = [-1] * n

        for i in range(n-1,-1,-1):
            while mon_stack and mon_stack[-1] < nums2[i]:
                mon_stack.pop()
            if mon_stack:
                nxt_greater[i] = mon_stack[-1]
            mon_stack.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(nxt_greater[nums2.index(num)])
        return ans
            
                

