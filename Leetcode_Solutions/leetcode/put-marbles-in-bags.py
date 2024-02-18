class Solution:
  def putMarbles(self, weights: List[int], k: int) -> int:

    A = [a + b for a, b in itertools.pairwise(weights)]
    return sum(heapq.nlargest(k - 1, A)) - sum(heapq.nsmallest(k - 1, A))