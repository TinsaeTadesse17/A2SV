class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    ans = 0
    max_num = 0
    vowels = 'aeiou'

    for i, c in enumerate(s):
      if c in vowels:
        max_num += 1
      if i >= k and s[i - k] in vowels:
        max_num -= 1
      ans = max(ans, max_num)

    return ans