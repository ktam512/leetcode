public class Solution {
    public boolean canJump(int[] nums) {
        // The farthest index that can be reached
        int maxReachable = 0;
        
        // Iterate through each index in the array
        for (int i = 0; i < nums.length; i++) {
            // If the current index is beyond the maximum reachable index, return false
            if (i > maxReachable) {
                return false;
            }
            // Update the maximum reachable index if the current index plus its value is greater
            maxReachable = Math.max(maxReachable, i + nums[i]);
            // If the maximum reachable index is beyond or at the last index, return true
            if (maxReachable >= nums.length - 1) {
                return true;
            }
        }
        
        // If the loop finishes without reaching the end of the array, return false
        return false;
    }
}
