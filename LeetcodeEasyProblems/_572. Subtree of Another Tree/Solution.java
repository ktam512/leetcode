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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // If the subRoot are null, always return true
        if (subRoot == null){
            return true;
        }
        // if the root is empty while the subRoot is not, 
        // then return false
        if (root == null){
            return false;
        }
        // Now knowning that both of them are not empty
        // check if they are the same tree
        if (this.sameTree(root, subRoot)){
            return true;
        }
        // If they're not, then check the left and right subtree
        return this.isSubtree(root.left, subRoot)
        || this.isSubtree(root.right, subRoot);
        
    }

    public boolean sameTree(TreeNode p, TreeNode q){
        // If the root are both null, return true
        if (p == null && q == null){
            return true;
        }
        // If either of them are empty, return false
        if(p == null || q == null){
            return false;
        }
        // Now we know that they're both not empty
        // Check if their root.val are the same
        // If they're not, return false
        if (p.val != q.val){
            return false;
        }
        // Now we know that their root.val are the same
        // We can only return true when both their left 
        // and right subtree are the same
        return this.sameTree(p.left, q.left) && this.sameTree(p.right, q.right);
    }
}