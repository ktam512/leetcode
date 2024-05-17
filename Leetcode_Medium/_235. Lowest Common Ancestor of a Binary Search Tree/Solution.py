# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Start from the root node of the tree
        current = root
        
        # Traverse the tree
        while current:
            # If both p and q are greater than current node
            if p.val > current.val and q.val > current.val:
                # Go to the right subtree
                current = current.right
            # If both p and q are less than current node
            elif p.val < current.val and q.val < current.val:
                # Go to the left subtree
                current = current.left
            else:
                # We have found the split point, i.e. the LCA node
                return current
        