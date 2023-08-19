public class Solution {
    public static void main(String[] args) {
        int[] prices = new int[]{5,6,3,7,8,4};
        System.out.println(maxProfit(prices));
    }
    public static int maxProfit(int[] prices) {

        int minVal = Integer.MAX_VALUE;
        int maxProfit = 0;

        for(int i = 0; i< prices.length;i++){
            if(prices[i] < minVal){
                minVal = prices[i];
            } else if(prices[i] - minVal > maxProfit){
                maxProfit = prices[i] - minVal;
            }
        }

        return maxProfit;




    }


}