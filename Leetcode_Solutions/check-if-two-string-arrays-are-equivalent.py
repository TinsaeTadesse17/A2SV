class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word = ""
        words = ""
        for i in range(len(word1)):
            word+=word1[i]
        for j in range(len(word2)):
            words+=word2[j]
        if word == words:
            return True
        else:
            return False
