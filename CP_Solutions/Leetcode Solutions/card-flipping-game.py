class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        s = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.add(fronts[i])

        nums = fronts + backs
        ans = []

        for num in nums:
            if num not in s:
                ans.append(num)

        return min(ans) if ans else 0