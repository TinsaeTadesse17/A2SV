class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        count = 1

        for i,char in enumerate(word):
            if i < len(word) - 1 and word[i] == word[i+1] and count < 9:
                count += 1
            else:
                ans += str(count) + char
                count = 1
        return ans

            
