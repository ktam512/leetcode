## Common error:

- After running the isUnivalTree function for left subtree and rightsubtree, it’s easy to forget that even when the left or right subtree is null, the function isUnivalTree still return true.
    - The lesson is be aware of the return type of the function: In this case, very likely one assume that the right subtree or left subtree exist simply because it passed through the function.
- That’s why we have to do another check:
    - The destination at the end:
    
    ```python
    if root.val == root.right.val and root.val == root.left.val:
                return True
    ```
    
    - We have to make sure that:
        - When reach this point, both the left and right subtree are univalued
        - However, this doesn’t take away the possibility of them being null
        - Therefore, another check: if either one of them is null, it only return true if the existing other side have the same value as the root (because it will throw an error NoneType if we try to call for the value when the node is null: root.right.val or root.left.val)

## Key

- In the end, it’s a similar problem to many dfs problems, but with a little change.
- Be aware of the return type of function. Does calling the function take away the possibility of them being null?