class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for val,count in counter.items():
            if val == 0:
                ans += count
            elif count <= val + 1:
                ans += val + 1
            else:
                ans += ceil(count / (val+1)) * (val+1)

        return ans
        
