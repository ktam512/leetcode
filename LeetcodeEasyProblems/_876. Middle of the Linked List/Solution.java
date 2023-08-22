/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode current = head;
        int count = lengthLinkedList(head)/2 + 1;
        while(count != 0){
            current = current.next;
            count--;
        }

        return current;
        
    }

    public int lengthLinkedList(ListNode head) {
        int count = 0;
        ListNode current = head;

        while(current!= null){
            count++;
            current = current.next;
        }
        return count;
    }
}