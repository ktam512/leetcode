class Solution {
    public int trap(int[] height) {
        // Initialize the length of the array
        int n = height.length;
        // Initialize the two pointer
        int left = 0;
        int right = n - 1;
        // Intialize the two maxLeft and maxRight array
        int maxLeft = height[left];
        int maxRight = height[right];
        // Intialize the result total trapped water
        int trappedWater = 0;
        // Run the loop until two pointer meet each other
        while (left < right){
            if (maxLeft < maxRight){
                left++;
                maxLeft = Math.max(maxLeft, height[left]);
                trappedWater += maxLeft - height[left];
            } else {
                right--;
                maxRight = Math.max(maxRight, height[right]);
                trappedWater += maxRight - height[right];
            }
        }

        return trappedWater;

        
    }
}