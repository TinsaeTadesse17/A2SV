class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = Counter(s1)
        left , right = 0 , len(s1)
        while right <= len(s2):
            if hashmap == Counter(s2[left:right]):
                return True
            right += 1
            left += 1
        return False
