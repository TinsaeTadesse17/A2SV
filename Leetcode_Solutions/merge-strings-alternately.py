class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        num = min(len(word1), len(word2))
        for i in range(num):
            ans += word1[i]
            ans += word2[i]
        if len(word1) > len(word2):
            ans += word1[num:len(word1)]
        elif len(word1) < len(word2):
            ans += word2[num:len(word2)]

        return ans
        
        
        


    


        