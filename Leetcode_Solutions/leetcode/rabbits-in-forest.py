class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        nums = list(set(answers))
        for i in nums:
            ans += (i+1) * ceil(counter[i]/(i+1))
                
        return ans