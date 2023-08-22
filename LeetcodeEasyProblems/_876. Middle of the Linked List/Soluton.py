# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = self.length(head)//2 + 1
        current = head
        while count!= 1:
            current = current.next
            count-=1
        
        return current

        
    def length(self, head):
        count = 0
        current = head
        while current:
            count+=1
            current = current.next
        
        return count