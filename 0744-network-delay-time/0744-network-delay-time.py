class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        curr = [float("inf") for _ in range(n)]
        prev = [float("inf") for _ in range(n)]

        prev[k-1] = 0
        curr[k-1] = 0

        for i in range(n-1):
            for u , v, w in times:
                curr[v-1] = min(prev[u-1] + w , curr[v-1])

            prev = curr.copy()

        return max(curr) if max(curr) != float("inf") else -1
