# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        ans = 0

        xor2 = 0
        for num in nums2:
            xor2 ^= num

        for num in nums1:
            if n % 2 == 0:
                ans ^= xor2
            else:
                ans ^= num ^ xor2

        return ans
     