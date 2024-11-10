class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ans = ""
        tcount = defaultdict(int)
        scount = defaultdict(int)
        
        def check(scount,tcount):
            flag = True
            for val in tcount:
                if val not in scount or scount[val] < tcount[val]:
                    flag = False
                    break
            return flag

        for char in t:
            tcount[char] += 1
        
        left = 0
        for right in range(n):
            scount[s[right]] += 1
            
            while check(scount,tcount):
                if ans == "" or (ans != "" and right - left + 1 < len(ans)):
                    ans = s[left:right+1]
                scount[s[left]] -= 1
                if scount[s[left]] == 0:
                    del scount[s[left]]
                left += 1

        return ans


