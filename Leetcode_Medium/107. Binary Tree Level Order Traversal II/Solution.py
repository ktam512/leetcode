class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        q = deque()
        q.append(root)
        curLevelCount = 1
        nextLevelCount = 0

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
                res.append(currentLevel)
                currentLevel = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return reversed(res)