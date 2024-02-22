# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(root,key):
            
            def minValueNode(node):
                current = node

                while current.left:
                    current = current.left

                return current
            
            
            if root == None:
                return None
                    
            if key < root.val:
                root.left = delete(root.left,key)
                return root
            elif key > root.val:
                root.right =  delete(root.right,key)
                return root

            
            #case 1 and case 2 is handeled one or no child
            if not root.left:
                print(root.right)
                return root.right
            if not root.right:
                return root.left

            print("Nooooooo")
            temp = minValueNode(root.right)
            
            root.val = temp.val
            #delete the inorder successor
            root.right = delete(root.right,temp.val)

            return root
            

        return delete(root,key)
        


