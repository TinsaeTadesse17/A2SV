class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string = s1 + " " + s2
        arr = string.split(" ")
        counter = Counter(arr)

        ans = []
        for word, count in counter.items():
            if count == 1:
                ans.append(word)
        return ans
