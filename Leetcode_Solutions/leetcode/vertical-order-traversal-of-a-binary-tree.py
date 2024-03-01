# Definition for a binarb tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        mydict = defaultdict(list)

        def verticalTrav(root,a,b):
            if not root:
                return None

            mydict[a].append((-b,root.val))

            verticalTrav(root.left,a-1,b-1)
            verticalTrav(root.right,a+1,b-1)

        verticalTrav(root,0,0)

        for _,j in sorted(mydict.items(), key=lambda item: item[0]):
            ans.append([val for _, val in sorted(j)])

        return ans

