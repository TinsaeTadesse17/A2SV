class Solution:
    def canJump(self, nums: List[int]) -> bool:

        flag = True
        n = len(nums)-1

        for i in range(n-1,-1, -1):
            if nums[i] < n-i:
                flag = False
            else:
                flag = True
                n = i
        if flag:
            return flag
        return flag
            
                

