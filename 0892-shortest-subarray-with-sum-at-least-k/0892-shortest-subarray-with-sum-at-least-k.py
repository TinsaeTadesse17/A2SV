class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # indices of the prefix sums
        indices = deque()
        ans = float('inf')
        
        for i in range(n + 1):
            # valid?
            while indices and prefix_sum[i] - prefix_sum[indices[0]] >= k:
                ans = min(ans, i - indices.popleft())
            
            # increasing prefix sums
            while indices and prefix_sum[i] <= prefix_sum[indices[-1]]:
                indices.pop()
            
            indices.append(i)
        
        return ans if ans != float('inf') else -1
