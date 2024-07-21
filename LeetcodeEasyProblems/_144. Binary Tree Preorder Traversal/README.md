Common error:

- Know that this is a recursive problem, I attempted to make the function return type to be directly the array/ list. This is true for the return type of the answer, but when you called it recursively, it will actually return a nested array. (Example: [1, [2,3],[4,5])) which is not List[int]
- Beware of the difference between root.val and root. One is an integer variable while the other  is a TreeNode that contains the value that equals to that integer.

Key:

The key here is to create a helper function to modify an original array, without returning anything.

Then we will call this helper function recursively. That way, each time we call this function, it will only modify the array and not add another array inside of it.

Reference:

- This strategy of “calling a function to modify” is a common theme for tree problem. I will add more detail surrounding this strategy later.