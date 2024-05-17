# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # First set the current node to the head
        # of the linked list
        cur = head
        # Create a hash set to store all the visited nodes
        visited_nodes = set()
        # Run the loop following the .next method until
        # we reach the end of the linked list
        while (cur != None):
            # If the current node is already visited
            # Return True: we got a cycle
            if (cur in visited_nodes):
                return True
            # If the current node is not in the set,
            # add it 
            visited_nodes.add(cur)
            # Go to the next node
            cur = cur.next
        # If we do reach the end, there's no cycle
        return False

        
