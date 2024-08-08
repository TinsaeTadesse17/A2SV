from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word1 = set("qwertyuiop")
        word2 = set("asdfghjkl")
        word3 = set("zxcvbnm")

        ans = []
        for word in words:
            unique_chars = set(word.lower())  
            if unique_chars <= word1 or unique_chars <= word2 or unique_chars <= word3:
                ans.append(word)

        return ans
