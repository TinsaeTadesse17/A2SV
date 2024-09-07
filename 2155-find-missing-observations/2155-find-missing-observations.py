class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        
        missing_sum = (mean * (n + m)) - sum(rolls)
        # Check if it's possible to construct a valid sequence
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        result = []
        while missing_sum > 0:
            dice = min(missing_sum - n + 1, 6)  
            result.append(dice)
            missing_sum -= dice
            n -= 1
        
        return result