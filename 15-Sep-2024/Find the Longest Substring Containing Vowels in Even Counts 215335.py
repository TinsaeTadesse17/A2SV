# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        hashmap = {(0, 0, 0, 0, 0): -1}  
        a, e, i, o, u = 0, 0, 0, 0, 0
        
        max_length = 0
        
        for index, char in enumerate(s):
            if char == 'a':
                a = 1 - a  
            elif char == 'e':
                e = 1 - e
            elif char == 'i':
                i = 1 - i
            elif char == 'o':
                o = 1 - o
            elif char == 'u':
                u = 1 - u
            curr = (a, e, i, o, u)
            
            if curr in hashmap:
                max_length = max(max_length, index - hashmap[curr])
            else:
                hashmap[curr] = index
        
        return max_length
