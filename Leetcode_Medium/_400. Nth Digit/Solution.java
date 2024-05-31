class Solution {
    public int findNthDigit(int n) {
        // Initialize variables to track the size of number groups, starting number of each group, and the count of digits
        int size = 1;
        long count = 9;
        long start = 1;

        //Determine which group the nth digit belongs to
        while (n > size * count) {
            n -= size * count; // Subtract the total number of digits in previous groups
            size++; // Increment the size to move to the next group
            count *= 10; // Increase the count of digits per number group (1-9, 10-99, 100-999, etc.)
            start *= 10; // Update the starting number of each group
        }

        //Find the actual number where the nth digit is located
        long num = start + (n - 1) / size; // Calculate the number where the nth digit is located

        //Find the digit within the number
        return String.valueOf(num).charAt((n - 1) % size) - '0'; // Convert the number to string, find the nth digit, and convert it back to integer
    }
}
