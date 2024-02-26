class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(num):
            # process or output a candidate
            if  len(path) == k:
                ans.append(path[:])
                return
            # handle basecases
            # iterate all possible candidates.
            if num > n:
                return
           
            # try this partial candidate solution
            path.append(num)
            # given the candidate, explore further.
            if len(path) <= k:
                backtrack(num + 1)
            else:
                return
            # backtrack
            path.pop()

            backtrack(num + 1)

            return 


        backtrack(1)
        return ans
            

