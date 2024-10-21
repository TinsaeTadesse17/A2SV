class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        unique_set=set()
        count=0
        ans=0
        def backtrack(start, count):
            nonlocal ans
            if start==len(s):
                ans= max(ans, count)
            for end in range(start+1, len(s)+1):
                substring=s[start:end]
                if substring not in unique_set:
                    unique_set.add(substring)
                    backtrack(end, count+1)
                    unique_set.remove(substring)
            return ans
        backtrack(0,count)
        return ans