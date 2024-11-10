class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")
        arr = [0] * 32
        left = 0

        def bit_update(arr,n,diff):
            for i in range(32):
                    if n & (1 << i):
                        arr[i] += diff

        def bit_to_int(arr):
            bitwise_or = 0
            for i in range(32):
                if arr[i]:
                    bitwise_or += (1 << i)
            return bitwise_or
        

        for right in range(n):
            bit_update(arr,nums[right],1)
            bitwise_or = bit_to_int(arr)
            
            while left <= right and bitwise_or >= k:
                ans = min(ans,right-left+1)
                bit_update(arr,nums[left],-1)
                bitwise_or = bit_to_int(arr)
                left += 1
    
        return ans if ans != float("inf") else -1
            
