# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        curLevelCount = 1
        nextLevelCount = 0
        # This variable is used to store 
        # the rightmost value of the current level
        currentLevelRight = 0
        while q:
            node = q.popleft()
            if curLevelCount == 1:
                currentLevelRight = node.val
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            curLevelCount -=1
            if curLevelCount == 0:
                res.append(currentLevelRight)
                currentLevel = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return res