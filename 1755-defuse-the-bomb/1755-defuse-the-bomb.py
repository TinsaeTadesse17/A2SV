class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k > 0: 
            for i in range(n):
                j = i
                curr = 0
                for _ in range(k):
                    j += 1
                    curr += code[j%n]
                ans[i] = curr

        elif k < 0:
            for i in range(n):
                j = i 
                curr = 0
                for _ in range(abs(k)):
                    j -= 1
                    curr += code[j]
                ans[i] = curr

        return ans
        