class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(k):
            stores = 0
            #how many stores do I need if each can only take atmost k items
            for quantity in quantities:
                stores += ceil(quantity/k)
            return stores <= n #if less than or equal to the number of stores I have right now

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        return left
