# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        sums = []

        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            sums.append(level_sum)

        root.val = 0
        queue.append(root)
        k = 1

        while k < len(sums):

            next_sum = sums[k]

            for _ in range(len(queue)):

                node = queue.popleft()
                left_val = node.left.val if node.left else 0
                right_val = node.right.val if node.right else 0

                new_val = next_sum - left_val - right_val

                if node.left:
                    node.left.val = new_val
                    queue.append(node.left)

                if node.right:
                    node.right.val = new_val
                    queue.append(node.right)

            k += 1

        return root