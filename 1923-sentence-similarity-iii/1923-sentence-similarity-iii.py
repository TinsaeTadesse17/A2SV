class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        if len(sentence2) > len(sentence1):
            sentence1 , sentence2 = sentence2 , sentence1

        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        n , m = len(sentence1) , len(sentence2)

        f1 , b1 , f2 , b2 = 0 , n - 1 , 0 , m - 1

        while f1 < n and f2 < m and sentence1[f1] == sentence2[f2]:
            f1 += 1
            f2 += 1

        while b1 >= 0 and b2 >= 0 and sentence1[b1] == sentence2[b2]:
            b1 -= 1
            b2 -= 1

        return f2 == b2 + 1 or f2 > b2





