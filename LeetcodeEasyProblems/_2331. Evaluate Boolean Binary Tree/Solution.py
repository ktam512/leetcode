class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val
        leftEval = self.evaluateTree(root.left)
        rightEval = self.evaluateTree(root.right)
        if root.val == 2:
            return leftEval or rightEval
        else:
            return leftEval and rightEval