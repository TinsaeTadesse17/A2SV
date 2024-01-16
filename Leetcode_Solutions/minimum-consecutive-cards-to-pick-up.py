class Solution:
  def minimumCardPickup(self, cards: List[int]) -> int:
    ans = float("inf")
    lastSeen = {}

    for i, card in enumerate(cards):

      if card in lastSeen:
        ans = min(ans, i - lastSeen[card] + 1)

      lastSeen[card] = i

    return -1 if ans == float("inf") else ans