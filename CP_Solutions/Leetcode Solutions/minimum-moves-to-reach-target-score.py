class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles:
            if target & 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            count += 1

        return count + target - 1
                

        