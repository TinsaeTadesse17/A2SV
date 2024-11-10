class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        count = defaultdict(int)

        left = 0
        for right in range(n):
            count[s[right]] += 1

            for val in count:
                while count[val] > 1:
                    count[s[left]] -= 1
                    left += 1
            ans = max(ans,right-left+1)
            
        return ans
