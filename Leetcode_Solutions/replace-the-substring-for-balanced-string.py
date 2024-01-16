class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        n = len(s)
        ans = float("inf")
        left = 0

        for right,char in enumerate(s):
            counter[char] -= 1

            while left < n and all(counter[char] <= n//4 for char in "QWER"):
                ans = min(ans, right-left + 1)
                counter[s[left]] += 1
                left += 1

        return ans 
        
        
