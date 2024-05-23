import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Create a dummy node and a pointer to it
        ListNode dummy = new ListNode();
        ListNode current = dummy;
        
        // Priority queue to store ListNode objects
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        // Add the heads of all lists to the priority queue
        for (ListNode node : lists) {
            if (node != null) {
                pq.offer(node);
            }
        }
        
        // Merge lists using the priority queue
        while (!pq.isEmpty()) {
            // Poll the smallest value node
            ListNode node = pq.poll();
            
            // Append the node to the result list
            current.next = node;
            current = current.next;
            
            // Move to the next node in the popped list
            if (node.next != null) {
                pq.offer(node.next);
            }
        }
        
        return dummy.next;
    }
}
