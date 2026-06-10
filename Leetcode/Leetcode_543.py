"""
LeetCode 543. Diameter of Binary Tree

Problem:
Given the root of a binary tree, return the length of the
diameter of the tree.

The diameter of a binary tree is the length of the longest path
between any two nodes in a tree. This path may or may not pass
through the root.

The length of a path between two nodes is represented by the
number of edges between them.

Example:

        1
       / \
      2   3
     / \
    4   5

Output: 3

Explanation:
The longest path is:

4 -> 2 -> 1 -> 3

Number of edges = 3

---------------------------------------------------------
Approach: DFS + Height Calculation
---------------------------------------------------------

Observation:

For every node:

Diameter Through Current Node
=
Height of Left Subtree + Height of Right Subtree

Example:

        1
       / \
      2   3

left height  = 1
right height = 1

diameter through node 1
= 1 + 1
= 2

While computing heights using DFS, we update the maximum
diameter seen so far.

---------------------------------------------------------
Algorithm
---------------------------------------------------------

1. Create a variable 'diameter' to store the maximum answer.
2. Define a helper function height(node).
3. If node is None, return 0.
4. Recursively calculate:
      left_height
      right_height
5. Update:
      diameter = max(diameter,
                     left_height + right_height)
6. Return:
      1 + max(left_height, right_height)
7. Start DFS from root.
8. Return diameter.

---------------------------------------------------------
Dry Run
---------------------------------------------------------

Input:

        1
       / \
      2   3
     / \
    4   5

Node 4:
height = 1

Node 5:
height = 1

Node 2:
left  = 1
right = 1

diameter = 1 + 1 = 2

height(2) = 2

Node 3:
height = 1

Node 1:
left  = 2
right = 1

diameter = max(2, 2 + 1)
         = 3

Answer = 3

---------------------------------------------------------
Time Complexity
---------------------------------------------------------

O(n)

Each node is visited exactly once.

---------------------------------------------------------
Space Complexity
---------------------------------------------------------

O(h)

h = height of the tree

Recursion stack stores at most h calls.

Worst Case (Skewed Tree):
O(n)

Balanced Tree:
O(log n)

---------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        height(root)

        return diameter