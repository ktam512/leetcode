class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        // Loop 32 times through the bit of n
        for (int i = 0; i < 32; i++){
            // Check if the LSB of the current n
            // is 1 or not and count it
            if ((n & 1) == 1){
                count++;
            }
            n >>= 1;
        }
        return count;
        
    }
}