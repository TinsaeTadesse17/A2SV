from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        inorder = defaultdict(list)
        
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                inorder[root.val].append(0)
                inorder_traversal(root.right)
        
        inorder_traversal(root)
        
        max_count = max(len(v) for v in inorder.values())
        
        return [k for k, v in inorder.items() if len(v) == max_count]
