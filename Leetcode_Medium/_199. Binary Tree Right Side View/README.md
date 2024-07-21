## Key

- Very similar to

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

- In fact, one can only change this part:

```python
 if curLevelCount == 0:
                res.append(currentLevel[-1])
                currentLevel = []
                curLevelCount = nextLevelCount
                nextLevelCount = 0
```

- We do the same for the whole section, however, we only res.append(currentLevel[-1]). This means that we only add the last element of the currentLevel into the result array - which is the rightmost element.

However, do it this way means we have created the whole currentLevel array but only use 1 element inside of it.

- We can save memory by do it as the code above:
    - Create a new currentLevelRight variable to store only the rightmost element at each level
    - Only update it when curLevelCount == 1 - which means the node.val is the element we’re looking for