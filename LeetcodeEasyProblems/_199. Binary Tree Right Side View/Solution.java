 import java.util.ArrayList;
 import java.util.LinkedList;
 import java.util.List;
 import java.util.Queue;
 
 public class Solution {
 
     public List<Integer> rightSideView(TreeNode root) {
         List<Integer> rightNode = new ArrayList<Integer>();
         if (root == null) {
             return rightNode;
         }
         Queue<TreeNode> queue = new LinkedList<TreeNode>();
         queue.add(root);
         while (!queue.isEmpty()) {
             int size = queue.size();
             for (int i = 0; i < size; i++) {
                 TreeNode node = queue.poll();
                 if (i == size - 1) {
                     rightNode.add(node.val);
                 }
                 if (node.left != null) {
                     queue.add(node.left);
                 }
                 if (node.right != null) {
                     queue.add(node.right);
                 }
             }
         }
         return rightNode;
     }
 }
 
 class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;

 
     TreeNode(int x) {
         val = x;
     }
 }