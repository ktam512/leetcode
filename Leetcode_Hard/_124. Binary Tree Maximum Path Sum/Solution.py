class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node): # Return maxNonSplit
            if not node:
                return -pow(10, 4) - 1 # 
            leftNonSplit = dfs(node.left)
            rightNonSplit = dfs(node.right)
            maxNonSplit = max(node.val, max(leftNonSplit,rightNonSplit) + node.val)
            maxSplit = max(node.val, leftNonSplit + rightNonSplit + node.val)
            nonlocal res
            res = max(res, maxNonSplit, maxSplit)

            return maxNonSplit
        dfs(root)
        return res

