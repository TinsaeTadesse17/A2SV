class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        min_subarray = float("inf")
        prefix_indices = deque() #monotonic so that smallest prefix sum is always at the front

        for i,summ in enumerate(prefix_sum):
            while prefix_indices and summ - prefix_sum[prefix_indices[0]] >= k: #valid prefix sum, minimize length
                min_subarray = min(min_subarray,i-prefix_indices.popleft())

            while prefix_indices and summ <= prefix_sum[prefix_indices[-1]]: #smaller prefix sums correspond to earlier indices, and subtracting them minimizes the subarray length so pop until current prefix sum is the largest
                prefix_indices.pop()

            prefix_indices.append(i)

        return min_subarray if min_subarray != float('inf') else -1











        
        

            











        
        
