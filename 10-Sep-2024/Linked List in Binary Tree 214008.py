# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def match(head,root):
            if not head: # all matched 
                return True
            if not root: # tree done before matching all
                return False

            if root.val != head.val:
                return False

            return match(head.next,root.right) or match(head.next,root.left)

        return match(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)

