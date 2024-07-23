- This problem is very similar to

[[**102. Binary Tree Level Order Traversal**](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)]

and have similar ideas to 

[[**1315. Sum of Nodes with Even-Valued Grandparent**](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/)]

## Key

- The tricky part about this problem is the condition for strictly increasing and decreasing
    - At first, I tackle this by calling the sort() and sort(reverse = True) function at the end of the level and compare it to the currentLevel list. However, I soon realised that the array.sort() function modify the array itself, and return None.
    - Then I turn my attention to the 1315 problem - which also involve keeping track of other node and node.val at the same time to fullfill some kind of condition.
    - It’s the same idea here. You have to keep track of the previous node’s value to ensure the condition.

## My credit go to…

- Full disclosure though: my code is full of bug at first. ChatGPT helped me iron things out. Lesson: Don’t use GPT to cheat, but to learn. Much more rewarding that way.