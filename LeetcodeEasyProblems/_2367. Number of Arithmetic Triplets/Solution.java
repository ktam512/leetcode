import java.util.HashMap;

public class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        // HashMap to store the count of elements
        HashMap<Integer, Integer> count = new HashMap<>();
        // Variable to store the count of arithmetic triplets
        int tripletsCount = 0;

        // Initialize the count HashMap with the elements of nums
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Iterate through the elements of nums
        for (int num : nums) {
            // Calculate the previous numbers in the potential triplets
            int prevNum1 = num - diff;
            int prevNum2 = num - 2 * diff;

            // Check if both previous numbers exist in count
            if (count.containsKey(prevNum1) && count.containsKey(prevNum2)) {
                // Update tripletsCount with the count of valid triplets
                tripletsCount += count.get(prevNum1) * count.get(prevNum2);
            }
        }

        return tripletsCount;
    }
}