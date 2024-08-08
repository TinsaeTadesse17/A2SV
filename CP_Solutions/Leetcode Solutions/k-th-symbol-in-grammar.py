class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0

        def kthSymbol(n, k):
            nonlocal ans
            level_mid = 2 ** (n - 1) // 2

            if n == 1:
                return ans

            if k > level_mid:
                if ans == 0:  
                    ans = 1
                else:
                    ans = 0
                return kthSymbol(n - 1, k - level_mid)
            else:
                return kthSymbol(n - 1, k)

        return kthSymbol(n, k)
