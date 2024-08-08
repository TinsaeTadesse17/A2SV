class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums)-1
        
        while low < high:
            mid = (low+high)//2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid    
            else:
                return mid

        return low if nums[low] == target else -1
            