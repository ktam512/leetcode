- Again, a very similar problem to

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

## Key

- Going through with the bfs (level-order traversal) normally, we realize we have to get the next node inside the queue to connect it to: [node.next](http://node.next) = ???
    - The first method that comes to my mind is peek()
    - But after running it, I realize it doesn’t exist in python!
        - So I do some Google search, and for deque(), you can actually use index: queue[0] to get to the next element without removing it like popleft()

## Common error

- At the end of the level, we connect the last node on that level to None. That’s when we have to take into consideration the value of curLevelCount at that time. Easy to forget.