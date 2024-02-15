class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = counter[0]
        nums = list(set(answers))

        if 0 in nums:
            nums = nums[1:]
 
        for i in nums:
            if i == 1:
                ans += counter[1] + (counter[1] % 2)
            else:
                ans += (i+1) * ceil(counter[i]/(i+1))
                
        return ans