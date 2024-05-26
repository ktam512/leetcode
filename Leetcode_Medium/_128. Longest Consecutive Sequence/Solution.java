import java.util.HashSet;

public class Solution{

    public static int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        int maxLength = 0;

        // Add all numbers to the set
        for (int num : nums) {
            numSet.add(num);
        }

        // Iterate through the array
        for (int num : nums) {
            if (!numSet.contains(num - 1)) { // Check if the current number is the start of a sequence
                int currentNum = num;
                int currentLength = 1;

                // Count consecutive elements
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentLength++;
                }

                maxLength = Math.max(maxLength, currentLength); // Update max length
            }
        }

        return maxLength;
    }
}
