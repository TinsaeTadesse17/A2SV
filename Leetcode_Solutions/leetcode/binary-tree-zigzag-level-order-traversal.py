# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        flag = False

        while queue:
            current_level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not flag: 
                flag = True 
            else: 
                flag = False


            if flag:
                result.append(current_level)
            else:
                result.append(current_level[::-1])

        return result
