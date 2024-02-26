class Solution:
  def trap(self, height: List[int]) -> int:
    n = len(height)
    left = [0] * n  
    right = [0] * n  

    for i, h in enumerate(height):
      left[i] = h if i == 0 else max(h, left[i - 1])

    for i, h in reversed(list(enumerate(height))):
      right[i] = h if i == n - 1 else max(h, right[i + 1])

    return sum(min(left[i], right[i]) - h
               for i, h in enumerate(height))