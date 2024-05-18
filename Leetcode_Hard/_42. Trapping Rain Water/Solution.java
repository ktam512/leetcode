class Solution {
    public int trap(int[] height) {
        // Initialize the length of the array
        int n = height.length;
        // Intialize the two maxLeft and maxRight array
        int[] maxLeft = new int[n];
        int[] maxRight = new int[n];
        // Intialize the result total trapped water
        int trappedWater = 0;
        // Fill the maxLeft array
        for (int i = 1; i < n; i++ ){
            maxLeft[i] = Math.max(maxLeft[i-1], height[i-1]);
        }
        // Fill the maxRight array
        for (int i = n-2; i >= 0; i-- ){
            maxRight[i] = Math.max(maxRight[i+1], height[i+1]);
        }
        // Check the values of current water in a specific
        // position and add it to the total trapped water 
        // if it's positive
        for (int i = 0; i < n; i++){
            int curWater = Math.min(maxLeft[i], maxRight[i])- height[i];
            if (curWater > 0){
                trappedWater+=curWater;
            }
        }

        return trappedWater;

        
    }
}