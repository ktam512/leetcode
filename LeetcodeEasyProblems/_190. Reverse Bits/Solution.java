public class Solution {
    // you need treat n as an unsigned value
    public static int reverseBits(int n) {
        //Turn the integer n into the String for ease of changing it
        String bitInteger = String.valueOf(n);
        //If the entered number is not an 32 bit integer, return -1
        if (bitInteger.length() != 32){
            return -1;
        }
        //Create a placeholder character and an empty string
        char placeholderChar;
        String  reversedBitInteger = "";
        // The for loop to take each character in the original string 
        // mirror it through the central axis 
        for (int i = 31; i>=0;i--){
            placeholderChar = bitInteger.charAt(i);
            reversedBitInteger += placeholderChar;
        }
        // Convert the bit integer to its decimal counterpart and return it
        int reversedDecimalInteger = 0;
        for (int i = 31; i >=0; i --){
            placeholderChar = reversedBitInteger.charAt(i);
            if (i > 0) {
                reversedDecimalInteger+= (int)Math.pow(2,(31-i)) * Character.getNumericValue(placeholderChar);
            } else {
                // When the most significant digit of the bit is 1, then the sign is negative
                if (placeholderChar == 1){
                    reversedDecimalInteger -= (int)Math.pow(2,31);
                }
            }

        }
        return reversedDecimalInteger;
    }

    public static void main(String[] args) {
        System.out.println(reverseBits(00000010100101000001111010011100));
    }
}