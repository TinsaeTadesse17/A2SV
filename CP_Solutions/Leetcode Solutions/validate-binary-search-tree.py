# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        
        def postorder(root):
            nonlocal ans  

            if not root:
                return None
            
            left = postorder(root.left)
            right = postorder(root.right)
            
            if left and left[1] >= root.val:
                ans = False
            if right and right[0] <= root.val:
                ans = False
            
            temp = [0, 0]
            temp[0] = root.val if not left else left[0]
            temp[1] = root.val if not right else right[1]
            
            return temp

        postorder(root)
        return ans




     

        
