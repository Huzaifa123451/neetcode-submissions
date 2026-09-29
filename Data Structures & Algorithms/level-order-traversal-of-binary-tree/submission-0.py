# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst_to_return = []
        def dfs(node,depth):
            if not node:
                return None
            if len(lst_to_return) == depth:
                lst_to_return.append([])
            lst_to_return[depth].append(node.val)
            dfs(node.left,depth + 1)
            dfs(node.right, depth + 1)
        dfs (root, 0)
        return lst_to_return