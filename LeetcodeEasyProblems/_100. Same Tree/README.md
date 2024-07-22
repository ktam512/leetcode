(IMPORTANT PROBLEM, we will use it many time in later problems)
## Common error

- It’s very easy to forget all of the null option for both trees. Aside from the case that p and q exist and have values, we have 3 different case:
    - If both p and q are null, they are the same tree so return True
    - Two case: If either p or q is null, they are not the same tree so return False
- After handling this case, we can finally move on to calling recursive left and right as normal.
- Finally, noting that only when 3 things happen that we return true:
    - left subtree are same tree
    - right subtree are same tree
    - root’s value of both tree are equal