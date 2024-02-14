class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k > numOnes and k <= numOnes + numZeros:
            return numOnes
        elif k > numOnes + numZeros:
            return numOnes + (-1 * (k-(numOnes + numZeros)))
