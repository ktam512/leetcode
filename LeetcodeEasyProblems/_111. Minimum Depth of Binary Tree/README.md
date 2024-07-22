Important problem to learn to be careful!

This problem is similar to

[[**104. Maximum Depth of Binary Tree**](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)]
However, their similarity may confuse people.

## Common error:

- Even though it’s marked as easy, the logic of the problem is quite hard.
    - Normally, we often start with the assumption that if you reach a subtree with no node, then its depth is zero. We did the same in problem 104.
    - This assumption is right, however when you reach the return statement 1 + min(leftEval, rightEval), the min operation will return 0 if either one of them is null
    - However, if one side of the tree is null while the other is not, we only start counting the depth from the existing side.
    - Therefore, we must be careful, or else we will always return 1 (since min(0, a) == 0)