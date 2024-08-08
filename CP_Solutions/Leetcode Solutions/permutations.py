class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(nums):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                path.append(nums[i])
                backtrack(nums)
                path.pop()

        backtrack(nums)
        return ans
