class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] <= nums[i-1]:
                num = nums[i-1] - nums[i] + 1

                while not is_prime(num):
                    num += 1

                if num >= nums[i-1]:
                    return False
                else:
                    nums[i-1] -= num
        sorted_nums = sorted(nums)
        return sorted_nums == nums
        




