## Common error:

- This base case is a little special:
    - Because you’re dealing with a balance binary tree, a node will either have 0 or 2 children.
    - The base case is that the node is a leaf node, then we return its value directly
- Notice that because of the property of the balanced binary tree, you actually only need to evaluate either the root.left or root.right exist or not. Since if one exists, so does the others and vice versa:

Instead of:

```python
if not root.left and not root.right:
            return root.val
```

We can just write:

```python
if not root.left:
            return root.val
```

## Key

- The hint inside the leetcode section reveal that this is actually a post-order traversal
    - Which mean: left → right → root. That’s true in this case, since you take the boolean operation from left to right and bottom to top.

## More questions:

- Follow up questions: The base case here is special in that it’s the leaf node. Is this the same for other post-order traversal/ dfs problems?