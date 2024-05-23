import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int subarraySum(int[] nums, int k) {
        // Map to store the cumulative sum frequencies
        Map<Integer, Integer> sumCountMap = new HashMap<>();
        // Initial sum is 0 and there's one way to get sum 0, by not taking any elements
        sumCountMap.put(0, 1);
        
        int currentSum = 0;
        int count = 0;
        
        // Iterate over the array
        for (int num : nums) {
            // Update the current sum
            currentSum += num;
            
            // Check if there is a subarray (or multiple) ending at current position that sums to k
            if (sumCountMap.containsKey(currentSum - k)) {
                count += sumCountMap.get(currentSum - k);
            }
            
            // Update the map with the current sum
            sumCountMap.put(currentSum, sumCountMap.getOrDefault(currentSum, 0) + 1);
        }
        
        return count;
    }
}
