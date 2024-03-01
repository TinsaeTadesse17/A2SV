class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i,path,summation):
            if summation == target:
                ans.append(path.copy())
                return

            if i >= len(candidates) or summation > target:
                return

            path.append(candidates[i])
            backtrack(i,path,summation + candidates[i])
            path.pop()
            backtrack(i+1,path,summation)

        backtrack(0,[],0)
        return ans


            
