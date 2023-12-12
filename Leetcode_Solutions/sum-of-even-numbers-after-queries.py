class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum = 0

        for i in nums:
            if i % 2 == 0:
                sum+=i

        for j in queries:
            if nums[j[1]] % 2 == 0:
                sum-= nums[j[1]] 
            
            nums[j[1]] += j[0]

            if nums[j[1]] % 2 == 0:
                sum += nums[j[1]]
            ans.append(sum)

        return ans
         

            
       













        
