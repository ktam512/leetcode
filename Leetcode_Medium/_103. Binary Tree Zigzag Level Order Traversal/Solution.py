# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   def zigzagLevelOrder(self, root):
       """
       :type root: TreeNode
       :rtype: List[List[int]]
       """
       # Using the BFS function to have the nodes on each level
       # but at the odd level (1, 3, 5, ..)
       # reverse its order


       # If root == None
       if root == None:
           return []
       # If root != None
       # Add the root to the queue and
       # start going through each level
       queue = [root]


       # Intialize the result list to store
       result = []


       while queue:
           # The list of node in  each level
           level = []
           # Go through each node using the for loop
           for i in range(len(queue)):
               cur_node = queue.pop(0)
               # Add the nodes value to the level list
               level.append(cur_node.val)
               # Check the left and right node
               if cur_node.left:
                   queue.append(cur_node.left)
               if cur_node.right:
                   queue.append(cur_node.right)
           # If the current level is odd, reverse it
           if len(result) % 2 != 0:
               level.reverse()
           # Add the current level (reversed if odd)
           # to the result list
           result.append(level)
       return result