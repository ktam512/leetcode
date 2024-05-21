import java.util.PriorityQueue;
import java.util.Collections;

public class Solution {
    public int lastStoneWeight(int[] stones) {
        // Create a max-heap using a priority queue
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Add all stones to the max-heap
        for (int stone : stones) {
            maxHeap.add(stone);
        }
        
        // Process the stones until there is one or no stones left
        while (maxHeap.size() > 1) {
            // Extract the two heaviest stones
            int first = maxHeap.poll();
            int second = maxHeap.poll();
            
            // If the stones have different weights, insert the difference back into the heap
            if (first != second) {
                maxHeap.add(first - second);
            }
        }
        
        // Return the last remaining stone or 0 if no stones are left
        return maxHeap.isEmpty() ? 0 : maxHeap.poll();
    }
}
