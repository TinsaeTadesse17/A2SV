class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        segments = [] 

        curr_seg = []
        for num in nums:
            count = bin(num).count('1')
            if curr_seg and count != bin(curr_seg[-1]).count('1'):
                curr_seg =sorted(curr_seg)
                segments.append(curr_seg)
                curr_seg = [num]
            else:
                curr_seg.append(num)
        curr_seg =sorted(curr_seg)
        segments.append(curr_seg)

        for i in range(1, len(segments)):
            if segments[i - 1][-1] >= segments[i][0]: 
                return False
        return True

       
