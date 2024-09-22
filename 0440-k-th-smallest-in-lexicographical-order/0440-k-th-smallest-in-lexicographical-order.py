class Solution:
    def trie(self, n, curr):
        total = 0
        nxt = curr + 1
        while curr <= n:
            total += min(n - curr + 1, nxt - curr)
            curr *= 10
            nxt *= 10
        return total
    
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            nodes = self.trie(n, curr)
            if k >= nodes:
                curr += 1
                k -= nodes
            else:
                curr *= 10
                k -= 1

        return curr