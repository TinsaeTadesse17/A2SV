class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        curr = ""
        j = 0
        for i,char in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                curr += " "
                j += 1
            curr += char
        return curr
            