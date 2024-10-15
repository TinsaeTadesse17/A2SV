class Solution:
    def minimumSteps(self, s: str) -> int:
        count1 = 0
        min_steps = 0
        
        for char in s:
            if char == "1":
                count1 += 1
            else:
                min_steps += count1

        return min_steps

        
