class Solution {
    public int maxArea(int[] height) {
        // Initialize the two pointers
        int left = 0;
        int right = height.length-1;
        int maxVol = 0;
        while (left < right){
            int curVol = (right - left) 
            * Math.min(height[left], height[right]);
            maxVol = Math.max(maxVol, curVol);
            if (height[left] < height[right]){
                left++;
            }else{
                right--;
            }
        }

        return maxVol;
    }
}