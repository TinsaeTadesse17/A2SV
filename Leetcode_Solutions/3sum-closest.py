class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        result = nums[0] + nums[1] + nums[2]  

        for i in range(len(nums) - 2):
            a = i + 1
            b = len(nums) - 1

            while a < b:
                current_sum = nums[i] + nums[a] + nums[b]

                if current_sum > target:
                    b-= 1
                else:
                    a += 1

         
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum

        return result

