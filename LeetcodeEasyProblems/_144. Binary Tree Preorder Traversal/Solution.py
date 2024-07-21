# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preorder(root, output):
            # If the root is null //non-existent
            if root is None:
                return
            output.append(root.val)
            preorder(root.left, output)
            preorder(root.right, output)
        preorder(root, arr)
        return arr