/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // First check the case when both of them are null
        if (p == null && q == null){
            return true;
        }
        // If either one of them are null, return false
        if (p == null || q == null){
            return false;
        }
        // After solving the null case, if the values
        // are different in the root node, return false
        if (p.val != q.val){
            return false;
        }
        // Then move on to check the left and right subtree
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}