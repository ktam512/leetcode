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
        # First define the fast and slow pointers
        # and put them at the start of the list
        slow, fast = head, head
        # The speed of the slow pointer will be 1 nodes
        # per iteration, while the fast pointer will be 2

        # If they don't have a cycle, the fast pointer
        # will just reach the end of the linked list first

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False


        
