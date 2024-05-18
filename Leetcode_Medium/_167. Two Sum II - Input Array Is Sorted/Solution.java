class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Initialize two pointer at the start and end
        // of the array
        int left = 0;
        int right = numbers.length - 1;
        // The loop continue until left == right
        while (left < right){
            // Create a sum integer of left and right value
            int sumNum = numbers[left] + numbers[right];
            // If the value are smaller than the target
            // Also knowning that the array is sorted, we have 
            // to increase the index of left to increase the total
            // sumNum value
            if (sumNum < target){
                left ++;
            }else if(sumNum == target){
                int[] resArr = new int[2];
                resArr[0] = left+1;
                resArr[1] = right + 1;
                return resArr;
            } else{
                // If the value are bigger, then we reduce
                // the right pointer to make the total sum smaller
                right--;
            }
        }
        return new int[2];
        
    }
}