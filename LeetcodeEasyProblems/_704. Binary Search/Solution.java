class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        // Intialize the pointers
        int left = 0;
        int right = n - 1;
        // Keep running until two pointers meat each other
        while (left <= right){
            int mean = (left + right)/ 2;
            if (mean < target){
                left = mean + 1;
            } else if (mean > target){
                right = mean - 1;
            } else {
                return mean;
            }
        }
        return - 1; 
    }
}