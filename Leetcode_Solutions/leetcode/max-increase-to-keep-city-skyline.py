class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    row = list(map(max, grid))
    column = list(map(max, zip(*grid)))
    val1 = sum(min(i, j) for i in row for j in column)
    val2 = sum(map(sum, grid))
    return  val1 - val2