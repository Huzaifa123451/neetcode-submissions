# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root) == -1:
            return False
        else:
            return True

    def get_height(self,node):
        left_height = 0
        right_height = 0
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        if right_height == -1 or left_height == -1 or abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height,right_height)