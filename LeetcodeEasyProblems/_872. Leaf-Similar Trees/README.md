## Key

- It’s similar to the

[[**144. Binary Tree Preorder Traversal**](https://leetcode.com/problems/binary-tree-preorder-traversal/)]
- It’s also using DFS - which means recursivelt traverse through left and right chidlren.
- The dfs function in this case also only modify a data structure (in this case, an array)

## Common error:

- Writing the dfs function inside the main function allow us to call it directly, without having to use self. (Since it’s a local function inside the main function)
- Forget to check for the condition of the null node
    - The constraint may keep it from 0, but remember that as we write the dfs function, this recursive method will definitely reach the null leaves node.