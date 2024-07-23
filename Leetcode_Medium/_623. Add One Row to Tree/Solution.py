# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode()
            node.val = val
            node.left = root
            return node
        
        q = deque()
        q.append(root)
        curLevelCount = 1
        nextLevelCount = 0
        currentLevel = []
        level = 1
        while q:
            if level == depth - 1:
                node = q.popleft()
                newRowLeft = TreeNode()
                newRowLeft.val = val
                if node.left:
                    nextLevelCount += 1
                    newRowLeft.left = node.left
                node.left = newRowLeft

                newRowRight = TreeNode()
                newRowRight.val = val
                if node.right:
                    nextLevelCount += 1
                    newRowRight.right = node.right
                node.right = newRowRight

            else:
                node = q.popleft()
                if node.left:
                    nextLevelCount += 1
                    q.append(node.left)
                if node.right:
                    nextLevelCount += 1
                    q.append(node.right)
            curLevelCount -= 1
            if curLevelCount == 0:
                if level == depth - 1:
                    return root
                curLevelCount = nextLevelCount
                nextLevelCount = 0
                level += 1
        return root