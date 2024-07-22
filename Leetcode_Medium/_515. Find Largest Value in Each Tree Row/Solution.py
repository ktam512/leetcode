class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        curLevelCount = 1
        nextLevelCount = 0

        curMaxOfLevel = - pow(2,31)

        while q:
            node = q.popleft()
            curMaxOfLevel = max(curMaxOfLevel, node.val)
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            curLevelCount -= 1
            if curLevelCount == 0:
                res.append(curMaxOfLevel)
                curMaxOfLevel = - pow(2,31)
                curLevelCount = nextLevelCount
                nextLevelCount = 0
            
        return res
        