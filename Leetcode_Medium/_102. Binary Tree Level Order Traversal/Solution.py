# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #1th, we create a result list of lists to contain all the 
        #list of each nodes in each level of the tree
        res = []
        #2th, we check if the root is null or not so that we can do
        #some more processing
        if root == None:
            return res
        #3th, now we create a queue to store the values of each level of nodes 
        #from left to right
        queue = collections.deque()
        #4th, because we now know that the root exist, we add them to the queue
        queue.append(root)
        #5th, now we loop through the while loop as long as the queue is not empty
        #in another word, when we still have nodes inside the tree
        while queue:
            #6th, we create a list to hold all the value of nodes inside the current
            #level
            curLevel = []
            #7th, we find the size of the queue, which is the same as the number
            #of nodes on the current level
            size = len(queue)
            #8th, we loop through the current level's queue and add them to the
            #current level's list
            for i in range(size):
                #9th, we have to use popLeft() as the queue go as FIFO
                node = queue.popleft()
                curLevel.append(node.val)
                #10th, we then check if the child nodes of the current node
                #is empty or not
                #If it's not empty, add it to the queue so that in the next iteration
                #it will be add into the curLevel
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #11th, at the end of the for loop, we have a finished list
            #of the that level. Then we will add that list into the result
            res.append(curLevel)
        #12th, at the end of the while loop, return res

        return res



