class RecentCounter:

    def __init__(self):
        self.recentRequests = deque()
        
    def ping(self, t: int) -> int:

        self.recentRequests.append(t)

        while self.recentRequests[0] < t-3000:
            self.recentRequests.popleft()
        
        return len(self.recentRequests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)