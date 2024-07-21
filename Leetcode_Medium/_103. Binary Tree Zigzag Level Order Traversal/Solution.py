# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        q = deque()
        q.append(root)

        curLevelCount = 1
        nextLevelCount = 0
        zigzagOrder = 0

        currentLevel = []

        while q:
            node = q.popleft()
            currentLevel.append(node.val)
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            curLevelCount -= 1
            if curLevelCount == 0:
                if zigzagOrder % 2 == 1:
                    res.append(currentLevel[::-1])
                else:
                    res.append(currentLevel)
                currentLevel = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
                zigzagOrder += 1
        return res