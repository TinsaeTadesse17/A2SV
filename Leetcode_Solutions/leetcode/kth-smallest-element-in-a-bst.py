# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def smallestnums(root,k,nums):
            if not root:
                return
            nums.append(root.val)
            smallestnums(root.left,k,nums)
            smallestnums(root.right,k,nums)

            return nums

        smallestnums(root,k,nums)

        nums.sort()
        return nums[k-1]

        
            

        