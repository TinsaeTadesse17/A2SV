class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        for num in num_count:
            complement = k - num

            if complement in num_count:
                if complement == num:
                    count += num_count[num] // 2
                else:
                    count += min(num_count[num], num_count[complement])

                num_count[num] = 0
                num_count[complement] = 0

        return count