class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(list)
        inf = int(2 * 1e9)
        weights = defaultdict(lambda: defaultdict(int))
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            if w == -1:
                weights[u][v] = 1
                weights[v][u] = 1

        def dijkstra() -> (int, List[int]):
            parents = [-1 for _ in range(n)]
            priority_queue = [(0, source)]
            min_costs = [inf for _ in range(n)]
            confirmed = [False for _ in range(n)]
            
            while priority_queue:
                cost, cur = heapq.heappop(priority_queue)
                if confirmed[cur]: continue
                min_costs[cur] = cost
                confirmed[cur] = True
                
                for nei, weight in graph[cur]:
                    if weight == -1:
                        weight = weights[cur][nei]
                    nei_cost = cost + weight
                    if nei_cost < min_costs[nei]:
                        parents[nei] = cur
                        min_costs[nei] = nei_cost
                        heapq.heappush(priority_queue, (nei_cost, nei))
            
            paths = []
            curr = destination
            while curr != source:
                nxt = parents[curr]
                if weights[nxt][curr] >= 1 and weights[nxt][curr] < inf:
                    paths.append((nxt, curr))
                curr = nxt
            return (min_costs[destination], paths)

        def form_answer() -> List[List[int]]:
            ans = []
            for u, v, w in edges:
                if w == -1:
                    ans.append([u, v, weights[u][v]])
                else:
                    ans.append([u, v, w])
            return ans

        curr_min_cost, min_cost_path = dijkstra()
        while curr_min_cost != target:
            if curr_min_cost > target or len(min_cost_path) == 0:
                return []
            u, v = min_cost_path[0]
            diff = target - curr_min_cost
            weights[u][v] = weights[v][u] = weights[v][u] + diff
            min_cost_paths = set(min_cost_path)
            for u, v, w in edges:
                not_exist = (u, v) not in min_cost_paths and (v, u) not in min_cost_paths
                if w == -1 and not_exist:
                    weights[u][v] = weights[v][u] = inf
            curr_min_cost, min_cost_path = dijkstra()
        
        return form_answer()