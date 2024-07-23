# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        curLevelCount = 1
        nextLevelCount = 0
        level = 0
        prev_val = None
        while q:
            node = q.popleft()
            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if prev_val and node.val <= prev_val:
                    return False
            else:
                if node.val % 2 == 1:
                    return False
                if prev_val and node.val >= prev_val:
                    return False
            prev_val = node.val
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            curLevelCount -= 1
            if curLevelCount == 0:
                level += 1
                curLevelCount = nextLevelCount
                nextLevelCount = 0
                prev_val = None
        return True