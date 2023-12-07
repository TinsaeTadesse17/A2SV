class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        words.append(s[:spaces[0]])
        for i in range(1,len(spaces)):
          words.append(s[spaces[i-1]:spaces[i]])
        words.append(s[spaces[len(spaces)-1]:])
        return ' '.join(words)

            
