# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
       
        
        def rangeSum(root,low,high):
            if not root:
                return 0
            rangeSummation = 0
    
            if low <= root.val <= high:
                rangeSummation += root.val
            if root.val > low:
                rangeSummation += rangeSum(root.left,low,high)
            if root.val < high:
                rangeSummation +=rangeSum(root.right,low,high)
                
            return rangeSummation
            

        return rangeSum(root,low,high)
        
        