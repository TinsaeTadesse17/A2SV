class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        binary_xor = bin(xor)[2:]
        return binary_xor.count('1')