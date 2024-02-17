class Solution:
  def longestPalindrome(self, s: str) -> int:
    ans = 0
    count = collections.Counter(s)

    for letter in count.values():
      ans += letter if letter % 2 == 0 else letter - 1

    oddCount = any(letter % 2 == 1 for letter in count.values())
    return ans + oddCount