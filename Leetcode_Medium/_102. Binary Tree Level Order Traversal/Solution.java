import java.util.Queue;

import javax.swing.tree.TreeNode;

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        //First, we create a list of list to store our result
        //(which is a list of the values of each nodes on each level
        //of the tree, from left to right)
        List<List<Integer>> result = new ArrayList<>();
        //Second, we check if the root exist so that we can do some processing
        if (root == null){
            return result;
        }

        //Third, now that we know the root exist, to use BFS, we create
        //a queue to store the nodes' values of each level

        Queue<TreeNode> queue = new LinkedList<>();
        //Fourth, because you know that the root exist at level 1 of the tree,
        //add it to the queue
        queue.add(root);

        //5th, we while loop when the queue is not empty
        //or in another word, we still have customers to serve 
        //(The queue is first come first served, the queue is not empty yet
        //meaning that the tree still have remaining nodes)
        while(!queue.isEmpty()){
            //6th, we check how many tree nodes we have to process
            //in this iteration/ level of the tree
            //Note that the queue will be updated at the end of the loop each time
            int size = queue.size();
            //7th, now we need to make a list of all the nodes of the current 
            //level of the tree
            List<Integer> currentLevel = new ArrayList<>();
            //8th, Next, we iterate through the current level's queue 
            //and add them to the current level list
            //We already know the size of the queue
            for (int i = 0; i < size;i++){
                //9th, we memorize the removed element from queue and then add its value 
                //to the current level list. Repeat this action until the queue is empty
                TreeNode current = queue.remove();
                currentLevel.add(current.val);
                //10th, we check if the left node and right node
                //of the current TreeNode is empty.
                //If it's not, then we add them to the queue so that in the next interation of the 
                //while loop, it will be processed as well
                if(current.left != null){
                    queue.add(current.left);
                }
                if(current.right != null){
                    queue.add(current.right);
                }
            }

            //11th, after the for loop, we are done with the list
            //of current level. The final thing we have to do is add them 
            //to the result list

            result.add(currentLevel);

        }

        //12th, and in the end, return the list result containing all the 
        // list of each nodes in each level from left to right

        return result;


        
    }
}