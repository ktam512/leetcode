class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            if node.children:
                childrenArr = node.children
                nextLevelCount += len(childrenArr)
                qChild = deque(childrenArr)
                while qChild:
                    nodeChild = qChild.popleft()
                    q.append(nodeChild)
            curLevelCount -= 1
            if curLevelCount == 0:
                res.append(currentLevel)
                currentLevel = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return res