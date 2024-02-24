class Solution:
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    queue = deque()

    for card in reversed(sorted(deck)):
      queue.rotate()
      queue.appendleft(card)

    return list(queue)