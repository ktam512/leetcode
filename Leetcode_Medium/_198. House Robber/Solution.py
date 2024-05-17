class Solution {
    public int rob(int[] nums) {
        # We're gonna use 2 pointers to store 
        # the maximum ammount one can rob up to 
        # the element n-2 and n-1
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2   
    }
}