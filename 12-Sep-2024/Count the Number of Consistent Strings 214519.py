# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
                    break
            if flag:
                count += 1   
        return count