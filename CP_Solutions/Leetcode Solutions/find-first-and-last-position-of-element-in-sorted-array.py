class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstOccurrence(nums, target):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        def lastOccurrence(nums, target):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        first = firstOccurrence(nums, target)
        last = lastOccurrence(nums, target)
        return [first, last]
