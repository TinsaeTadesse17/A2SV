# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in node.children:
                stack.append(child)

        return ans[::-1]

        