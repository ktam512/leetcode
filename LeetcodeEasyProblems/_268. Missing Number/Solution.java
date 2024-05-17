import java.util.HashSet;
class Solution {
    public int missingNumber(int[] nums) {
        HashSet<Integer> numsSet = new HashSet<Integer>();
        for (int num : nums){
            numsSet.add(num);
        }

        for (int i = 0; i < nums.length+1;i++){
            if (!numsSet.contains(i)){
                return i;
            }
        }
        return -1;
    }
}