class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        ans = [-1] * n
        
        idx_map = {}
        stack = []

        for i in range(len(nums)):
            while len(stack) and nums[stack[-1]] < nums[i]:
                idx_map[stack.pop()] = i
                
            stack.append(i)

        for idx in idx_map.keys():
            ans[idx % n] = nums[idx_map[idx % n] % n]

        ans = ans[:n]

        return ans


            
