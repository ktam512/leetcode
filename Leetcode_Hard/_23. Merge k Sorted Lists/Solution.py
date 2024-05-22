class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Keep dividing the lists by 2
        # like the merge sort operation
        # and merge each of them together

        # This way, it will take kOlog(k) time
        # complexity just like merge sort itself

        # First handle the edge case when
        # the lists are empty, null or have only 1
        # linked-list
        if lists == None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # Take the middle index to divide the list
        mid_index = len(lists) // 2
        left = self.mergeKLists(lists[:mid_index])
        right = self.mergeKLists(lists[mid_index:])
        
        # Merge the two lists using the helper method
        self.mergeLists(left, right)

    def mergeLists(self, list1, list2):
        # Use a temporary node to keep track
        # of curNode
        tempNode = ListNode()
        curNode = tempNode
        # Run the while loop until either list1 or 
        # list2 meet their end
        while list1 and list2:
            # Append it to the result and 
            # move to the next node in list1
            # if the value of list 1 is smaller
            if(list1.val < list2.val):
                curNode.next = list1
                list1 = list1.next
            # Same as above, but vice versa
            else:
                curNode.next = list2
                list2 = list2.next
            # Move to the next node in the loop
            curNode = curNode.next
        # After escaping the loop, the leftover
        # value got appended to the end of the list
        if list1:
            curNode.next = list1
        elif list2:
            curNode.next = list2
        # Returning the merged list, starting from the next node
        return tempNode.next

solution = Solution()
merged_list = solution.mergeKLists([[1,4,5],[1,3,4],[2,6]])


