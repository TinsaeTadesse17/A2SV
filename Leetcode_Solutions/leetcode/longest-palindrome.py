class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        ans = 0
        oddCount = 0
        counter = Counter(s)
        for val in counter.values():
            if val % 2 == 0:
                ans += val
            else:
                ans += val - 1
        oddCount = any(x % 2 == 1 for x in counter.values())
        return ans + oddCount
