

public class Solution {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }

    /**
     * Definition for a binary tree node.
     **/

      public class TreeNode {
          int val;
          TreeNode left;
          TreeNode right;
          TreeNode() {}
          TreeNode(int val) { this.val = val; }
          TreeNode(int val, TreeNode left, TreeNode right) {
              this.val = val;
              this.left = left;
              this.right = right;
          }
      }

    public TreeNode invertTree(TreeNode root) {
        if(root == null){
            return root;
        }

        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);

        root.left = right;
        root.right = left;

        return root;








    }
}