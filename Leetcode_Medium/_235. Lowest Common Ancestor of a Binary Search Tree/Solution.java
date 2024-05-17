/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Start from the root node of the tree
        TreeNode current = root;

        // Traverse the tree
        while (current != null) {
            // If both p and q are greater than current node
            if (p.val > current.val && q.val > current.val) {
                // Go to the right subtree
                current = current.right;
            } 
            // If both p and q are less than current node
            else if (p.val < current.val && q.val < current.val) {
                // Go to the left subtree
                current = current.left;
            } 
            // We have found the split point, i.e. the LCA node
            else {
                return current;
            }
        }
        return null; // In case the tree is empty
    }
}