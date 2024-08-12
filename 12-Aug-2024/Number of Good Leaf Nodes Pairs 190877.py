# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def dfs(node):

            if not node:
                return []

            if not node.left and not node.right:
                return [1]
            
            right = dfs(node.right)
            left = dfs(node.left)

            for r in right:
                for l in left:
                    if r + l <= distance:
                        self.ans += 1
            
            right = [r+1 for r in right]
            left  = [l+1 for l in left]

            return right + left 

        dfs(root) 
        return self.ans       



