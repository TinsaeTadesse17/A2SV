# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0
    
        for char in s:
            if stack and stack[-1] == "b" and char == "a":
                ans += 1
                stack.pop()
            else:
                stack.append(char)
        return ans
