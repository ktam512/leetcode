IMPORTANT PROBLEM

- This will become a basis for many medium and hard problems in the future
## Common error

- Remember that the append() function is adding an integer VALUE into an array, not NODE

It’s easy (at least personally) to confuse:

```python
arr.append(node.val)
```

with:

```python
arr.append(node)
```

and then an error TypeMismatch pop up!

## Key

- Important problem, so remember each details carefully
- We need an result array to store the result. It will be a nested array, with each array inside it

represent a level

- Then a queue (why a queue? see below) to mark each node that is soon-to-be-popped. This means that it will go through all node inside the tree and pop each one out so that we can process it (append it into this level’s array)
- After that, 2 variable/ parameter curLevelCount and nextLevelCount to represent the current node on this level that we have to process left, and the node on the next level that we will have to process, respectively.
    - The curLevelCount starting point will be 1, as at the start of the loop, we have already added the root node to the queue. The nextLevelCount starting point will be 0, as we will count that throughout the loop (more on this at the point below).
    - About how to update each variable:
        - curLevelCount will be updated when it reach 0 - meaning all the node on this level has already been processed. This marks the point where we end this level and move to the next one. That’s when we have curLevelCount = nextLevelCount
        - nextLevelCount will be updated throughout the loop. Increment it each time we count the children of nodes of the current level. After passing its value to curLevelCount (when we move from the end of the current level to the next), reset it to 0 to start counting again.
- Finally, we need an array currentLevel to store the value of each node in this level
    - We updated this one at the start of each loop, by append the node value into it
    - At the transition phase (again, move from the current level to the next), we add it to the result array, marking the end of one level. Then reset it to an empty array again, awaiting the next level.