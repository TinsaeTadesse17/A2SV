# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def dfs(node, level, level_list):
            if len(level_list)-1 < level:
                level_list.append([])
            max_depth = level
            if node.left:
                max_depth = dfs(node.left, level + 1, level_list)
            if node.right:
                max_depth = max(max_depth, dfs(node.right, level + 1, level_list))
            level_list[level].append((node.val, max_depth))
            return max_depth

        level_list = []

        dfs(root, 0, level_list)
        
        node_dict = {}
        for i, n in enumerate(level_list):
            max_depth = 0
            max_depth_node = 0
            second_max_depth = 0

            for j in n:
                if max_depth <= j[1]:
                    second_max_depth = max_depth
                    max_depth = j[1]
                    max_depth_node = j[0]
                elif second_max_depth <= j[1]:
                    second_max_depth = j[1]

            for j in n:
                if j[0] == max_depth_node:
                    if second_max_depth == 0:
                        node_dict[j[0]] = i-1
                    else:
                        node_dict[j[0]] = second_max_depth
                else:
                    node_dict[j[0]] = max_depth
        
        result = []
        for i in queries:
            result.append(node_dict[i])


        return result
