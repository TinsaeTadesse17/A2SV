class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        count = [0] * 32

        for candidate in candidates:
            pos = 0
            while candidate:
                if candidate & 1:
                    count[pos] += 1

                candidate >>= 1
                pos += 1

        return max(count)