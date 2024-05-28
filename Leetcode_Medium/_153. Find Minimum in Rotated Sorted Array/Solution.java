public class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) { // If mid element is greater than last, pivot lies to right of mid
                left = mid + 1;
            } else { // Otherwise, pivot lies to left of or at mid
                right = mid;
            }
        }
        return nums[left]; // Return element at left index as minimum
    }
}
