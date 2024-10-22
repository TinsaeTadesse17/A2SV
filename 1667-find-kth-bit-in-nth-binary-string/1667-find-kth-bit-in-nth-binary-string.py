class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def findBit(nums, n):
            if n == 1:
                return nums
            
            reverse_nums = nums[::-1]
            inverted_nums = ''.join('1' if c == '0' else '0' for c in reverse_nums)
            
            return findBit(nums + '1' + inverted_nums, n - 1)
        
        ans = findBit("0", n)
        
        return ans[k - 1]