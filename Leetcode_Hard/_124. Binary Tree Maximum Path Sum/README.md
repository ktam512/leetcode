## Common error

- It’s easy to calculate the maxNonSplit or maxSplit wrong. Remember: maxNonSplit must only take the bigger on in the leftNonSplit, rightNonSplit and add that to the current node value.
    - However, we also have to compare it to the current node value again because the max(leftNonSplit, rightNonSplit) can be negative.
    - As such, we have two options: Either choose 1 of the 2 children (if they exist) to create a path with the current node or choose to start from the node itself

## Key

- There’s 3 ideas here:
    - The idea of writing a dfs function to traverse, modify both variable and scenarios
    - The idea of using very small number (often -float’int’)
    - The idea of going from one node to another using a local variable