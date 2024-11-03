class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        pivot = s[0]
        ans = False

        for i,char in enumerate(goal):
            if char == pivot:
                ans = goal[i:] + goal[:i] == s
                if ans:
                    break

        return ans

