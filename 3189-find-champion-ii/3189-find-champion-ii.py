class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = defaultdict(int)
        for x , y in edges:
            incoming[y] += 1
            
        ans = []
        for node in range(n):
            if incoming[node] == 0:
                ans.append(node)
        return ans[0] if len(ans) == 1 else -1