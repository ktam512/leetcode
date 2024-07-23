- This problem is very similar to

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

## Key

- This problem is mostly the same as 102, but with a twist:
    - Because you have to keep track both parent and grandparent of a node now in order to react when the grandparent satisfy the condition
    - I did it this way by keeping a list of 3 element (node, parent, grandparent)
        - After this, it’s the same as 102