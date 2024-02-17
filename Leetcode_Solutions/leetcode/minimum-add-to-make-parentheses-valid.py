class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    left = 0
    right = 0

    for char in s:
      if char == '(':
        left += 1
      else:
        if left == 0:
          right += 1
        else:
          left -= 1

    return left + right