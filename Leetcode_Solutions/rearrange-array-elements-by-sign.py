class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num <= 0]

       
        ans = []
        for p, n in zip(pos, neg):
            ans.append(p)
            ans.append(n)

        return ans