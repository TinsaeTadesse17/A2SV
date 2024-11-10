class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        deq = deque()
        max_vals = []

        for i in range(n):
            if deq and deq[0] == i - k:
                deq.popleft()
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)
            
            if i >= k - 1:
                max_vals.append(nums[deq[0]])

        return max_vals