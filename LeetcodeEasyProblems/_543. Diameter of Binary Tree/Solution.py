# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        def maxDepth(node):
            if not node:
                return 0

            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            
            # Update the maximum diameter using the current node's depth
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the current node's subtree
            return 1 + max(left_depth, right_depth)

        # Initialize the diameter to 0
        self.diameter = 0

        # Start the recursive traversal from the root
        maxDepth(root)
        
        # Return the calculated diameter
        return self.diameter


