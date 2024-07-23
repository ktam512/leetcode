# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curMaxLvSum = pow(-10, 5)
        q = deque()
        q.append(root)
        curLevel  = 1
        resultLevel = 0
        curLevelCount = 1
        nextLevelCount = 0
        curLevelSum = 0

        while q:
            node = q.popleft()
            curLevelSum += node.val
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            curLevelCount -= 1
            if curLevelCount == 0:
                if curLevelSum > curMaxLvSum:
                    curMaxLvSum = curLevelSum
                    resultLevel = curLevel
                curLevelSum = 0
                curLevel += 1
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return resultLevel