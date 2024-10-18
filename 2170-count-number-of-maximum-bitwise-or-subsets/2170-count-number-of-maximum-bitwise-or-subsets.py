class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #Max OR of an array is the OR of the whole array
        max_or = 0
        for num in nums:
            max_or |= num

        self.count = 0

        #dfs for every subset
        def dfs(idx,curr_or):

            if idx == len(nums):
                if curr_or == max_or:
                    self.count += 1
                return

            #we consider two cases: to include the num or not to include it on curr_or

            dfs(idx+1 , curr_or | nums[idx])

            dfs(idx+1 , curr_or)

        dfs(0,0) #start at index 0 and bitwise OR zero(empty subset)

        return self.count