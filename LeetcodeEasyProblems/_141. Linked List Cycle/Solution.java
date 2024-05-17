/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // We tackle the case when the head is null
        if (head == null){
            return false;
        }
        // We create the slow and fast pointers
        ListNode slow = head;
        ListNode fast = head;
        // Use the while loop to check
        // if the next Node and the second node from the 
        // current fast pointers are not null (the end of the list)
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (slow.equals(fast)){
                return true;
            }

        }
        // If the fast pointer simply reach the end
        // of the linked list first, then
        //there's no cycle
        return false;

        
    }
}