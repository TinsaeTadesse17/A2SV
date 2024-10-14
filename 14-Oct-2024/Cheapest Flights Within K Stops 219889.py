# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prev = [float("inf") for _ in range(n)]
        curr = [float("inf") for _ in range(n)]

        prev[src] = 0
        curr[src] = 0


        for i in range(k+1):
            for u , v , w in flights:
                curr[v] = min(prev[u] + w , curr[v])
                
            prev = curr.copy()


        return curr[dst] if curr[dst] != float("inf") else -1