public class Solution {
    public int numDecodings(String s) {
        // Check if the input string is empty or starts with '0',
        // in which case it can't be decoded.
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0;
        }
        
        int n = s.length();
        // Create an array to store the number of ways to decode
        // the string up to the current index.
        int[] dp = new int[n + 1];
        
        // Initialize the first two elements of dp based on the
        // first digit of the input string.
        dp[0] = 1;  // Empty string has one way to decode
        dp[1] = s.charAt(0) != '0' ? 1 : 0;  // First digit can be decoded if it's not '0'
        
        // Iterate through the string starting from the second index.
        for (int i = 2; i <= n; i++) {
            // Check if the current single digit can be decoded
            // (i.e., it's between '1' and '9').
            if (s.charAt(i - 1) != '0') {
                dp[i] += dp[i - 1];  // Add the number of ways to decode the previous digit
            }
            
            // Check if the current two digits can be decoded
            // (i.e., they form a number between 10 and 26).
            int twoDigit = Integer.parseInt(s.substring(i - 2, i));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];  // Add the number of ways to decode the two previous digits
            }
        }
        
        // The last element of dp contains the total number of ways
        // to decode the entire string.
        return dp[n];
    }
}
