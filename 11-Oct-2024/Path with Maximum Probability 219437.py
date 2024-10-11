# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        m = len(edges)
        adj = defaultdict(list)
        for i in range(m):
            adj[edges[i][0]].append((edges[i][1],succProb[i]))
            adj[edges[i][1]].append((edges[i][0],succProb[i]))
        probabilities = [float("-inf") for _ in range(n)]
        probabilities[start_node] = 1
        
        queue = deque([(1,start_node)])

        while queue:
            prob , node = queue.popleft()

            for neigh , succProb in adj[node]:
                if probabilities[node] * succProb > probabilities[neigh]:
                    probabilities[neigh] = probabilities[node] * succProb
                    queue.append((probabilities[neigh], neigh))

        return probabilities[end_node] if probabilities[end_node] != float("-inf") else 0
                


