# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        binary_xor = bin(xor)[2:]
        return binary_xor.count('1')