- This problem is very similar to

[[**124. Binary Tree Maximum Path Sum**](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)]

## Common error

- It’s easy to forget that we have to let res to be a nonlocal veriable, or else they will not be interactable in the class
- The function to calculate and update res: res = max(res, leftPath + rightPath) have already containe the 2 edge that connect the current node to its children

## Keys

- Write a dfs funtion to traverse through the node, expecially when we face problems with checking children and parent
- There’s many path that will cut off on purpose, so we have to chane it