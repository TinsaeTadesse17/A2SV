# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ancestorDiff(node, minimum, maximum):
            if not node:
                return 0
                
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            
            diff1 = ancestorDiff(node.left, minimum, maximum)
            diff2 = ancestorDiff(node.right, minimum, maximum)
            
            return max(abs(node.val - minimum), abs(node.val - maximum), diff1, diff2)
        
        return ancestorDiff(root, root.val, root.val)
