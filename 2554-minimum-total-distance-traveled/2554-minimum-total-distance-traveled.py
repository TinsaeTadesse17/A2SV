class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        # Sort robots and factories for optimal pairing
        robots.sort()
        factories.sort()
        
        # Expand factories based on capacity
        expanded_factories = []
        for position, capacity in factories:
            expanded_factories.extend([position] * capacity)

        # Initialize DP table with infinity, and a base case row of zeros at the end
        dp = [[float("inf")] * (len(expanded_factories) + 1) for _ in range(len(robots) + 1)]
        dp[-1] = [0] * (len(expanded_factories) + 1)

        # Populate DP table from the bottom up
        for i in range(len(robots) - 1, -1, -1):
            for j in range(len(expanded_factories) - 1, -1, -1):
                distance = abs(expanded_factories[j] - robots[i])
                dp[i][j] = min(distance + dp[i + 1][j + 1], dp[i][j + 1])

        return dp[0][0]
