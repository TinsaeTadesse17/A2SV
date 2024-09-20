class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in range(n):
            if s[i] == s[n-j-1]:
                i += 1
        if i == n:
            return s
        palindrome = s[i:n][::-1]
        return palindrome + self.shortestPalindrome(s[:i]) + s[i:]