class Solution:
    def kthCharacter(self, k: int) -> str:
        def next(char):
            return chr((ord(char) - 95 ) % 26 + 96)
        next_count = 0
        size = 1
        while size < k :
            size *= 2
        def kth(size,k,next_count):
            if k == 1:
                ans = "a"
                if next_count:
                    for _ in range(next_count):
                        ans = next(ans)
                return ans
            if k > size // 2:
                return kth(size//2, k - size//2, next_count + 1)
            else:
                return kth(size//2, k, next_count)
            
            
        return kth(size,k,next_count)
