class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def change(pas, tot):
            return (pas + 1) / (tot + 1) - pas / tot
    
        max_heap = []
        for pas, tot in classes:
            heapq.heappush(max_heap, (-change(pas, tot), pas, tot))

        for _ in range(extraStudents):
            chng,pas,tot = heapq.heappop(max_heap)
            pas += 1
            tot += 1
            chng = -change(pas,tot)
            heapq.heappush(max_heap,(chng,pas,tot))
        ratio_sum = 0
        for change,pas,tot in max_heap:
            ratio_sum += pas/tot
        return ratio_sum / len(classes)




