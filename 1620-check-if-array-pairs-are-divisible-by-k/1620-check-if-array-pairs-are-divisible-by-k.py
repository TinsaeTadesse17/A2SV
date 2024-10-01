class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mydict = defaultdict(int)
        count = 0

        for i in arr:
            remainder = i % k

            if mydict[remainder] > 0:
                mydict[remainder] -= 1
                count += 1
            else:
                mydict[(k - remainder) % k] += 1
        
        return count == len(arr) // 2