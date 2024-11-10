class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = defaultdict(int)
        ans = 0

        def checker(counter):
            sorted_counter = sorted(counter.items(),key = lambda item : item[1] , reverse = True)
            max_num = sorted_counter[0][0]
            count = 0
            for val,cnt in sorted_counter:
                if val != max_num:
                    count += cnt

            return count

        left = 0
        for right in range(n):
            counter[s[right]] += 1
            if checker(counter) == k:
                ans = max(ans,right-left+1)
            while checker(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            

        return ans if ans != 0 else len(s)





