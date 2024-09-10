# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True , 0

            left_flag , left_height = dfs(root.left)
            right_flag , right_height = dfs(root.right)

            return abs(left_height-right_height) <= 1 and left_flag and right_flag , max(left_height,right_height) + 1
            

        return dfs(root)[0]