class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for _ in range(k):
            curr = max(gifts)
            gifts[gifts.index(curr)] = sqrt(curr) // 1

        return int(sum(gifts))