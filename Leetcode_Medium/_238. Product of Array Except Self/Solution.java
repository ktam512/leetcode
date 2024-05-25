class Solution {
  public int[] productExceptSelf(int[] nums) {
    final int n = nums.length;
    int[] ans = new int[n];    // Initialize array to store the final answer
    int[] prefix = new int[n]; // Initialize array to store the prefix product
    int[] suffix = new int[n]; // Initialize array to store the suffix product

    // Calculate prefix products
    prefix[0] = 1;
    for (int i = 1; i < n; ++i)
      prefix[i] = prefix[i - 1] * nums[i - 1];

    // Calculate suffix products
    suffix[n - 1] = 1;
    for (int i = n - 2; i >= 0; --i)
      suffix[i] = suffix[i + 1] * nums[i + 1];

    // Calculate final answer by multiplying prefix and suffix products
    for (int i = 0; i < n; ++i)
      ans[i] = prefix[i] * suffix[i];

    return ans; // Return the final answer array
  }
}
