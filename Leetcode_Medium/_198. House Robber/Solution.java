class Solution {
    public int rob(int[] nums) {
        // Define the length of the array
        int n = nums.length;
        //If the array have no element, return 0
        if (n == 0) return 0;
        //If the array have 1 element, rob that house
        if (n == 1) return nums[0];

        //Create an array with the same length as nums
        //each element will stored the maximum number one can rob 
        //up until that element from the start
        int[] dp = new int[n];
        //Copy the first element of nums
        //(since the maximum ammount one can rob up to the first house
        //is the value of the first house)
        dp[0] = nums[0];
        //The second element is the maximum one can rob up until 
        //the second house, which is between the first and second
        dp[1] = Math.max(nums[0], nums[1]);
        //A for loop to develop from those too instances:
        // Each element will be calculated by comparing
        //1) the maximum one can get up to the previous element
        //2) the sum of the maximum one can get up two element behind and in this case
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }

        //After the loop, return the desired element, at the end of the array
        
        return dp[n - 1];
    }
}
