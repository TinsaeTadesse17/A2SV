class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)//2):
            freq = nums[i*2]
            val = nums[2*i+1]
            for i in range(freq):
                arr.append(val)
        
        return arr