class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        flag = True
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                flag = False
                break

        return  words[0][0] == words[-1][-1] and flag
            
            