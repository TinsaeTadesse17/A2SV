class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        counter = Counter(arr)
        return counter.most_common()[0][0]