class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)
        
        map_nums1 = {num: i for i, num in enumerate(nums1)}
        
        for val in nums2:
            while stack and stack[-1] < val:
                top = stack.pop()
                if top in map_nums1:
                    ans[map_nums1[top]] = val
            stack.append(val)
        
        return ans
