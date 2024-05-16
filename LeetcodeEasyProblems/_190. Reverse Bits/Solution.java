public class Solution {
    // you need treat n as an unsigned value
    public static int reverseBits(int n) {
        // Check if the interger is 32 bit 
        //if it's not, return -1
        if (Integer.toString(n).length() != 32){
            return -1;
        }
        //Create the first bit of the result
        int result = 0;
        // The loop iterate 32 times to add 
        // each bit to the reversed bit
        for (int i = 0; i < 32; i++){
            //Shift the result by 1 to the left to wait for the next bit
            result <<= 1;
            // Take the least significant digit of the bit n and put it 
            // to the right side of the bit result
            result |= (n & 1);
            //Shift the bit n by 1 to the right to create room for the next bit
            n >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(reverseBits(00000010100101000001111010011100));
    }
}