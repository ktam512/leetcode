import java.util.PriorityQueue;

public class KthLargest {
    private int k;  // Store the value of k
    private PriorityQueue<Integer> minHeap;  // Initialize a min-heap

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();
        
        // Add each number in nums to the heap
        for (int num : nums) {
            add(num);
        }
    }

    public int add(int val) {
        minHeap.offer(val);  // Add the new value to the heap
        if (minHeap.size() > k) {  // If heap size exceeds k
            minHeap.poll();  // Remove the smallest element
        }
        return minHeap.peek();  // The smallest element in the heap is the kth largest
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */