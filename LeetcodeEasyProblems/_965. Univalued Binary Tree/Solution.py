class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        evalLeft = self.isUnivalTree(root.left)
        evalRight = self.isUnivalTree(root.right)
        if not evalLeft or not evalRight:
            return False
        root.left = root if not root.left else root.left
        root.right = root if not root.right else root.right
        if root.val == root.right.val and root.val == root.left.val:
            return True
        return False