class Solution {
    public int maxArea(int[] height) {
    
        int n = height.length;
        int curMaxVol = 0;
        // Using the nested for loop to sort through 
        // each water volume 
        for (int i1= 0; i1 < n - 1; i1++){
            for(int i2 = i1+1; i2 < n; i2++){
                int curWidth = Math.abs(i2 - i1);
                int curHeight = Math.min(height[i1], height[i2]);
                int curVolume = curWidth * curHeight;
                curMaxVol = Math.max(curMaxVol, curVolume);
            }
        }

        return curMaxVol;
        
    }
}