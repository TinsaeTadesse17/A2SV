# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def postorder(root):
            if not root:
                return [float('inf'), float('-inf'), 0]  

            left = postorder(root.left)
            right = postorder(root.right)

            if left and right and left[1] < root.val < right[0]:  
                sum_val = root.val + left[2] + right[2]  
                self.max_sum = max(self.max_sum, sum_val) 
                return [min(left[0], root.val), max(right[1], root.val), sum_val]  

            return [float('-inf'), float('inf'), 0] 

        postorder(root)
        return self.max_sum

        




     

        
