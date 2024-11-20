class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        tot_count = Counter(s)
        if len(tot_count) < 3 or any(count < k for count in tot_count.values()):
            return -1
        extra_count = defaultdict(int)
        window_width, left = 0, 0
        for right, ch in enumerate(s):
            extra_count[ch] += 1
            while tot_count[ch] - extra_count[ch] < k:
                extra_count[s[left]] -= 1
                left += 1
            window_width = max(right - left + 1, window_width)
        return len(s) - window_width