# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # When the subroot is null, they are always 
        # the subtree of the root node tree
        if subRoot == None:
            return True
        # When the subroot is not null, while the root node is null
        # then return false
        if root == None:
            return False
        # Now after knowning that the root and subroot
        # are not null, check if they are the same tree
        if self.sameTree(root,subRoot):
            return True
        # Now branch out the left and right subtree of root node
        left_root = root.left
        right_root = root.right
        # And check if there's a subtree in them
        return self.isSubtree(left_root, subRoot) or self.isSubtree(right_root, subRoot)
    def sameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # First we check if the root node is both null
        if p == None and q == None:
            return True
        # Check if either one of them is null
        if p == None or q == None:
            return False
        # Check if their values are different
        if p.val != q.val:
            return False
        return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
        