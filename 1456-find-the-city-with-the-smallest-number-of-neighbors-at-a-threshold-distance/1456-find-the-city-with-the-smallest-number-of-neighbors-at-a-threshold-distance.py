class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:   
        #floyd-warshall
        m = len(edges) 
        for i in range(m):
            u , v , w = edges[i]
            edges.append([v,u,w])

        matrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        for u , v , w in edges:
            matrix[u][v] = w
            matrix[v][u] = w


        for k in range(n):
            for i in range(n):
                if k == i:
                    continue
                for j in range(n):
                    if k == j:
                        continue
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])
        
        min_reach = n
        bestCity = -1
        
        for i in range(n):
            reach = sum(1 for j in range(n) if matrix[i][j] <= distanceThreshold)
            
            if reach <= min_reach:
                min_reach = reach
                bestCity = i
        
        return bestCity