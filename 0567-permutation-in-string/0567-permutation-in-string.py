class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n , m = len(s2) , len(s1)
        count1 = Counter(s1)

        for i in range(n-m+1):
            if Counter(s2[i:i+m]) == count1:
                return True
        return False

