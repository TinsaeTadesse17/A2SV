# Definition for a binary treeroot.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        def validBST(root, lower_bound=float('-inf'), upper_bound=float('inf')):
            if not root:
                return True

            if root.val <= lower_bound or root.val >= upper_bound:
                return False

            return validBST(root.left, lower_bound, root.val) and validBST(root.right, root.val, upper_bound)

        return validBST(root)
