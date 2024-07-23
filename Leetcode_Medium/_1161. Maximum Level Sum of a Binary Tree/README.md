- This is very similar to

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

## Key

- The only difference to 102 is that we have to keep track of the curMaxLvSum.
- Notice that the constraint is taken into account: We set the initial value for curMaxLvSum to be the smallest value possible (since from the example, we knew that there’s negative value)