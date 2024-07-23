# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sumResult = 0
        q = deque()
        q.append((root,None,None))
        curLevelCount = 1
        nextLevelCount = 0

        while q:
            node,parent,grandparent = q.popleft()
            if grandparent and grandparent.val % 2 == 0:
                sumResult += node.val
            if node.left:
                nextLevelCount += 1
                q.append((node.left, node, parent))
            if node.right:
                nextLevelCount += 1
                q.append((node.right, node, parent))
            curLevelCount -= 1
            if curLevelCount == 0:
                curLevelCount = nextLevelCount 
                nextLevelCount = 0
            
        return sumResult