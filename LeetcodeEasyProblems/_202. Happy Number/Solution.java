import java.util.HashSet;
class Solution {
    public boolean isHappy(int n) {
        // Create a visited hash map to 
        // keep track of each visited number
        HashSet<Integer> visitiedArr = new HashSet<>();
        while (!visitiedArr.contains(n)){
            // Add the number to visited array
            visitiedArr.add(n);
            // Update n into the sum of its
            // digit squared
            n = this.sumSquareDigit(n);
        }
        // After the loop, n become a value 
        // that's visited
        if (n == 1){
            return true;
        }
        return false;
        
    }
    public int sumSquareDigit(int number){
        // Initialize the sum of its digit squared
        int sum = 0;
        while (number != 0){
            // Add the digit squared to the sum
            sum += (number%10) * (number%10);
            // Update the number to the one without 
            // the digit
            number /= 10;
        }

        return sum;
    }
}