class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use a dictionary to store a level : index
        # Store the index of the first node at each level
        # 1:1, 2:2, 3: 4
        first_id_at_level = {}
        self.curMaxWidth = 0
        def dfs(node, level, index):
            if not node:
                return
            if level not in first_id_at_level:
                first_id_at_level[level] = index
            curWidth = index - first_id_at_level[level] + 1
            self.curMaxWidth = max(curWidth, self.curMaxWidth)

            dfs(node.left, level + 1, 2* index)
            dfs(node.right, level + 1, 2* index + 1)
        
        dfs(root, 1, 1)
        return self.curMaxWidth