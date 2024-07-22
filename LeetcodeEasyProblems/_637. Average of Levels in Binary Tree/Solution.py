class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        q = deque()
        q.append(root)
        curLevelCount = 1
        curLevelNum = 1
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
                averageCurLevel = sum(currentLevel) / curLevelNum
                currentLevel = []
                res.append(averageCurLevel)
                curLevelCount = nextLevelCount
                curLevelNum = nextLevelCount
                nextLevelCount = 0
            
        return res