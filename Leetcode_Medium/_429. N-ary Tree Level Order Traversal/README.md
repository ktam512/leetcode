This problem is similar to the 

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

problem. However, there’s some properties of n-ary tree that is different to binary one.

That’s why we have to make changes when come to those differences

## Clarification

- The properies of a n-ary tree is that its node can have mutiples children instead of only two like binary tree.
- Its children are stored under the name self.children and they’re a lists of Node.

## Key

- The difference between binary and n-ary tree will also determine the difference in the execution of our code.
- Instead of only considering and counting left and right child, count all the node by calling all children by if node.children:
    - After that, adding all the children into the nextLevelCount
    - Then we change the list of child node into a queue, so that we can pop it out and add them into our level queue in the right order
    - Aside from that, everything else stays the same