## Key

- A BFS problem, traverse to the (depth - 1) level and start adding new node with the provided value to fill out the depth level

## Common error

- It’s easy to forget that you can return the tree after adding all the node at the depth level
    - In fact, I wasted 15 min before realizing that I don’t have to think of way to fix the countNum, since there’s no level left to travel anyway.