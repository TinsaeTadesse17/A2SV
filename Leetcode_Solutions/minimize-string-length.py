class Solution:
    def minimizedStringLength(self, s: str) -> int:
        counter = Counter(s)
        return len(counter.keys())
            
        

        