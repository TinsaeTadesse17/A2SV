class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [[0] * n for _ in range(n)]
        
        for i in range(n):
            arr[i][i] = nums[i]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                arr[i][j] = max(nums[i] - arr[i+1][j], nums[j] - arr[i][j-1])
        

        return arr[0][n-1] >= 0
