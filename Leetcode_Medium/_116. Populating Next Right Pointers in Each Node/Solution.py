"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque()
        q.append(root)

        curLevelCount = 1
        nextLevelCount = 0

        while q:
            node = q.popleft()
            if curLevelCount > 1:
                node.next = q[0]
            elif curLevelCount == 1:
                node.next = None
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            
            curLevelCount -= 1
            if curLevelCount == 0:
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return root