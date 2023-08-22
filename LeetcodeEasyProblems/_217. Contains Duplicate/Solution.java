public class Solution {
    public boolean containsDuplicate(int[] nums) {
        for (int i = 0; i< nums.length;i++){
            int right = nums.length - 1;
            int left = i + 1;
            while(right!= left){
                if(nums[right] == nums[i]){
                    return true;
                } else {
                    right--;
                }

                if(nums[left] == nums[i]){
                    return true;
                } else {
                    left++;
                }




            }
        }

        return true;
        
    }
}