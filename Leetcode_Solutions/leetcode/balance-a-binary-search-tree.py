# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(root, inorder):
            if not root:
                return
            inorderTraversal(root.left, inorder)
            inorder.append(root.val)
            inorderTraversal(root.right, inorder)

        inorder = []
        inorderTraversal(root, inorder)

        def buildBalancedBST(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(inorder[mid])
            node.left = buildBalancedBST(left, mid - 1)
            node.right = buildBalancedBST(mid + 1, right)

            return node

        return buildBalancedBST(0, len(inorder) - 1)


        
            


        