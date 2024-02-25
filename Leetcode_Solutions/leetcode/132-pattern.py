class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if not stack or num < stack[-1][0]:
                stack.append((num, num))
            else:
                min_val = stack[-1][0]
                while stack and num > stack[-1][0]:
                    _, max_val = stack.pop()
                    if num < max_val:
                        return True
                stack.append((min_val, num))
        return False
