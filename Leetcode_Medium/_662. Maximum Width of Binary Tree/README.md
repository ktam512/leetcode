## Key

- This problem involves a helper function dfs. This helper function does not return, but only update the variable and data structure we’re using. (In this case, it’s the dictionary and the maxWidth variable)
    - This is similar to
    
    [[**144. Binary Tree Preorder Traversal**](https://leetcode.com/problems/binary-tree-preorder-traversal/)]
    
- This problem involves a dictionary/ hashmap to keep track of the key-value pair: level - index
    - Why do we do this? This dictionary store the index of the first node of each level
        - This way, we can have this index at hand to calculate the width created by the first node and the node we’re dealing with at the moment
- We also keep track of the global variable curMaxWidth. We change and update this variable when we traverse through the tree with the dfs function. Notice that it’s global (self.curMaxWidth). Only this way that we can update it using the dfs function.
- About the DFS function:
    - It got the parameter node - to indicate the current node that we’re dealing with
        - If that node is null, simply return nothing
        - Otherwise, it’s a tool (the same as node.left and node.right) for us to traverse through the tree
    - It got the parameter level - to indicate the current level we’re dealing with
        - Notice that the level of the root node can be either 1 or 0 - it will not change the results. Simply means that other node’s level will be changed accordingly
        
    - It got the parameter index - to indicate the index of the node we’re dealing with
        - This is the key point to measure the width: index - first_index_of_level
        - Similar to level, the root node index can be either 1 or 0
            - Personally, I will put it to be 1, so there’s no confusion between the first node (1 : 1) and the second node (2: 2). Otherwise, it will be (1: 0) and (2:0)
        
    - The final point: the properties of the binary tree. If we a particular node A have index i, then
        - node A.left have index 2 * i
        - node A.right have index 2 * i + 1