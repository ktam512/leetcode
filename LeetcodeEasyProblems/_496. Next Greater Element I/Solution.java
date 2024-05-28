import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>(); // Store mapping of elements to their next greater element
        Stack<Integer> stack = new Stack<>(); // Store indices of elements
        
        // Iterate through nums2 to find the next greater element for each element
        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }
        
        // Iterate through nums1 to retrieve next greater elements
        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = map.getOrDefault(nums1[i], -1); // If no next greater element found, store -1
        }
        
        return nums1;
    }
}
