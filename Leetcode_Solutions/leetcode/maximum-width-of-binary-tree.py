# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mydict = {}
        self.max_diff = 0
        
        def widthOfBinary(root, index, level, mydict):
            if root is None:
                return 
            mydict.setdefault(level, [index, index])
            mydict[level][0] = min(mydict[level][0], index)
            mydict[level][1] = max(mydict[level][1], index)
            self.max_diff = max(self.max_diff, mydict[level][1] - mydict[level][0])

            widthOfBinary(root.left, 2*index, level+1, mydict)
            widthOfBinary(root.right, 2*index+1, level+1, mydict)

        widthOfBinary(root, 0, 0, mydict)
        return self.max_diff+1