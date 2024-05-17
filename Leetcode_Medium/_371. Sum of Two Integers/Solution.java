class Solution {
    public int getSum(int a, int b) {
        // We're gonna use bit manipulation
        // in this solution
        // We noticed that the bitwise operator
        // OR can yield the same result before 
        // carrying as adding two bit together
        while(b!=0){
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}