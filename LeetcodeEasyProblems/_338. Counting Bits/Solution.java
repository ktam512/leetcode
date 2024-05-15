public class Solution {
    public static void main(String[] args) {
        int n = 5; 
        int[] result = countBits(n);
        
        for (int i : result) {
            System.out.print(i + " ");
        }
    }

    public static int[] countBits(int n) {
        int[] ans = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            ans[i] = countOnes(i);
        }
        
        return ans;
    }
    
    public static int countOnes(int num) {
        int count = 0;
        
        while (num > 0) {
            if ((num & 1) == 1) {
                count++;
            }
            num = num >> 1;
        }
        
        return count;
    }
}
