class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []

        for num in nums:
            heapq.heappush(heap,-num)
        
        for _ in range(k):
            num = heapq.heappop(heap)
            score += -1 * num
            heapq.heappush(heap,-1 * (ceil((-1 * num)/3)))
        return score



