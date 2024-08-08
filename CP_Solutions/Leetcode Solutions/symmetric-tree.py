# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)
        
        if not root:
            return True
        
        return checkSymmetry(root.left, root.right)