## Key

- This problem involve using the function directly to invert each part of the tree from top to bottom (Basically using dfs)
- The standard way of switching root.left and root.right is the same as above. The logic is the same for all kind of code
    - However, python have a way to shorten it:
    root.left, root.right = root.right, root.left