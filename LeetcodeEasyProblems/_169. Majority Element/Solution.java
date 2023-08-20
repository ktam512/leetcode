public class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        for (int element : nums){
            if (count == 0){
                candidate = element;
            }
            if(candidate == element){
                count++;
            }else{
                count--;
            }

        }

        return candidate;
    }
}
