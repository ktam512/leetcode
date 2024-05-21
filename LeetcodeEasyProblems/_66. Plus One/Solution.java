public class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        // Iterate from the last digit to the first
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // Set the current digit to 0 if it is 9
            digits[i] = 0;
        }
        
        // If all digits are 9, we need an extra digit at the beginning
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        return newDigits;
    }
}
