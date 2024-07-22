## Common error

- A big error that I made is not reading the constraint.
    - It’s -2^31 < node.val < 2^31. I put the inital value for curMaxOfLevel to be 0, and I messed up at a test when they have one node with -1 value alone at 1 level

## Key

- This is very similar to the

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)](https://www.notion.so/102-Binary-Tree-Level-Order-Traversal-d85d1cbb55dd4815a7b114e29a93bc06?pvs=21)

- You only have to change the currentLevel array to the curMaxOfLevel variable