class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        ans = float("inf")

        while left + k-1 < len(blocks):

            counter = Counter(blocks[left:left + k])
            ans = min(ans,counter['W'])
            left += 1

        return ans if ans != float("inf") else 0