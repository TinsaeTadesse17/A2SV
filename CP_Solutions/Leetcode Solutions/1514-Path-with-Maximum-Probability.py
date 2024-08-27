class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            src , dest = edges[i]
            graph[src].append([dest,succProb[i]])
            graph[dest].append([src,succProb[i]])


        priority_queue = [(-1 , start_node)] #tryna build a max heap as the probability as comparison key
        visited = set()

        while priority_queue:
            succ_prob , curr_node = heapq.heappop(priority_queue)
            visited.add(curr_node)

            if curr_node == end_node:
                return -1 * succ_prob

            for neighbor , edge_prob in graph[curr_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue,(succ_prob * edge_prob , neighbor))

        return 0





        