# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_num = max(interval[1] for interval in intervals)
        
        arr = [0] * (max_num + 2)  
        
        for i, j in intervals:
            arr[i] += 1
            arr[j + 1] -= 1
        
        running_sum = 0
        max_overlap = 0
        
        for k in range(max_num + 1):
            running_sum += arr[k]
            max_overlap = max(max_overlap, running_sum)
        
        return max_overlap