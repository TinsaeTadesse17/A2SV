# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maxBinaryTree(nums):
            if not nums:
                return None
            
            maxNum = max(nums)
            maxIndex = nums.index(maxNum)
            root = TreeNode(maxNum)
            root.left = maxBinaryTree(nums[:maxIndex])
            root.right = maxBinaryTree(nums[maxIndex + 1:])
            
            return root

        return maxBinaryTree(nums)
