class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque([i for i in range(n)])
        ans = 0
        while True:
            idx = queue.popleft()
            tickets[idx] -= 1
            if tickets[idx] > 0:
                queue.append(idx)
            ans += 1
            if tickets[k] == 0:
                return ans
