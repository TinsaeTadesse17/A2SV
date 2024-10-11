class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        m = len(edges)
        for i in range(m):
            edges[i].append(succProb[i])
        for i in range(m):      
            edges.append([edges[i][1] , edges[i][0] , succProb[i]])


        curr = [float("-inf") for _ in range(n)]
        prev = [float("-inf") for _ in range(n)]
        ans = 0

        prev[start_node] = 1
        curr[start_node] = 1

        for i in range(n-1):
            for u , v , w in edges:
                curr[v] = max(prev[u] * w , curr[v])
                if v == end_node:
                    ans = max(ans,curr[v])

            if prev == curr:
                break
            prev = curr.copy()

        return ans 





