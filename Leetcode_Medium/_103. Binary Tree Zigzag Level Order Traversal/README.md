- Very similar to
    
    [[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]
    
- The only difference is that we have to reverse the order of the currentLevel array in-between
- The solution is to keep track of a new variable (in this case, zigzagOrder) to know when to reverse the list. (Notice that doing this, we can expand the problem into reverse after 2, 3 ,… n level) (Not only revese, but we can process the array on a specific level, as long as it have some kind of pattern)