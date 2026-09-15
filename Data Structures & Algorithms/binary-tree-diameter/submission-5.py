class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0 

        def get_maxPath(node):
            if node is None:
                return 0
            
            left = get_maxPath(node.left)
            right = get_maxPath(node.right)
            
            # Update the global maximum diameter found so far
            self.maxPath = max(self.maxPath, left + right)
            
            # Return the height of the current node
            return 1 + max(left, right)

        get_maxPath(root)
        return self.maxPath