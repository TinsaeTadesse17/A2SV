class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return k
        tot_counter = Counter(s)
        if len(tot_counter) < 3 or any(cnt < k for cnt in tot_counter.values()):
            return -1 

        window_counter = Counter()
        left = 0
        window_size = 0
        for right,char in enumerate(s):
            window_counter[char] += 1

            while tot_counter[char] - window_counter[char] < k:
                window_counter[s[left]] -= 1
                left += 1
            window_size = max(window_size,right-left+1)
        return len(s) - window_size

