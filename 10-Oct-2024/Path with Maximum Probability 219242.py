# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        probabilities = {node: float('-inf') for node in range(n)}
        probabilities[start_node] = 1  

        heap = [(-1, start_node)] 
        processed = set()

        while heap:
            succ_prob, curr_node = heapq.heappop(heap)
            succ_prob *= -1  

            if curr_node == end_node:
                return succ_prob

            for neighbor, edge_prob in graph[curr_node]:
                new_prob = succ_prob * edge_prob  
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))  

        return 0  