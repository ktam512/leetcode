class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftEval = self.minDepth(root.left)
        rightEval = self.minDepth(root.right)
        if leftEval == 0:
            return rightEval + 1
        if rightEval == 0:
            return leftEval + 1
        return 1 + min(leftEval, rightEval)