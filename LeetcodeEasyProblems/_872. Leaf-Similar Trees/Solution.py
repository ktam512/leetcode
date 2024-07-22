class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []
        def numLeaves(node, output):
            if not node:
                return
            if not node.left and not node.right:
                output.append(node.val)
            numLeaves(node.left, output)
            numLeaves(node.right, output)
            return output
        numLeaves(root1, arr1)
        numLeaves(root2,arr2)
        return arr1 == arr2