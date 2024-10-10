class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start_node,end_node,weight in times:
            graph[start_node].append((end_node , weight))
        
        distances = {node: float('inf') for node in range(1, n + 1)}
            
        distances[k] = 0
        processed = set()

        heap = [(0, k)]
        while heap:
            distance , curr_node = heapq.heappop(heap)

            processed.add(curr_node)
            
            for child , weight in graph[curr_node]:
                if distance + weight < distances[child]:
                    distances[child] = distance + weight
                    heapq.heappush(heap,(distance + weight,child))
            
        return max(distances.values()) if max(distances.values()) != float('inf') else -1
        