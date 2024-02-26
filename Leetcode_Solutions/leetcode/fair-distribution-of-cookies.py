class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.unfairness = float("inf")
        buckets = [0] * k
        if len(cookies) == k:#pruning
            return max(cookies)

        def backtrack(i,buckets):
            
            if i >= len(cookies):
                # process or output a candidate
                self.unfairness= min(self.unfairness,max(buckets))
                return 
            if max(buckets) > self.unfairness:#pruning
                return    
            # handle basecases
            # iterate all possible candidates.
            for j in range(k):
                # try this partial candidate solution
                
                buckets[j] += cookies[i]
                # given the candidate, explore further.
                backtrack(i+1,buckets)
                # backtrack
                buckets[j] -= cookies[i]
                

        backtrack(0,buckets)
        return self.unfairness