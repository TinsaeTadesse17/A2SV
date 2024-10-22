class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = 0

        for i , char in enumerate(word):
            if char in vowels:
                ans += (i + 1) * (n - i)
        return ans