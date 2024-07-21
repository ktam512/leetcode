# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # When the root is null / non-existent
        if not root:
            return []
        res = []
        # The parameter to keep track of the number
        # of nodes we have to deal with in this level
        # At the end of the loop (see below),
        # we will pop the number of node out equal
        # to this curLevelCount
        # It starts with 1, since at this current level
        # we have only 1 node: the root
        curLevelCount = 1
        # This parameter keep track of the 
        # number of node on the next level
        # Know this by counting the number of chidlren
        # of each node at this level
        # At the end of the loop, we update the current level
        # count to this one, while it return to 0 (to count again)
        nextLevelCount = 0
        # The array that will store the 
        # value of node on this level
        # it will be filled out by receiving node
        # that we pop from the queue
        # At the end of the loop, we will add this
        # array/list to the result array, completing one level
        curLevelVal = []
        # The queue that will store the node that we 
        # visited/ counted on one level
        # When the node pop out of the queue, it means
        # we recorded that node into the curLevelNode

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            curLevelVal.append(node.val)
            # We count the number of node 
            # next level by counting
            # the children of the node on
            # this level
            if node.left:
                nextLevelCount += 1
                q.append(node.left)
            if node.right:
                nextLevelCount += 1
                q.append(node.right)
            # At each end of the loop,
            # we will decrement the curLevelCount
            # (we just pop it out at the start)
            curLevelCount -=1
            # Then check if all the node on this level
            # has been popped out
            if curLevelCount == 0:
                res.append(curLevelVal)
                # Reset the curLevelVal, 
                # cause we are done with this level
                curLevelVal = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
        return res



