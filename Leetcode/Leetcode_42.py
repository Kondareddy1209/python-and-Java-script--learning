"""
===========================================================
42. Trapping Rain Water
LeetCode: https://leetcode.com/problems/trapping-rain-water/

Difficulty: Hard

===========================================================
Problem Statement
===========================================================

Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it can trap
after raining.

Example:

Input:
height = [4,2,0,3,2,5]

Output:
9

Explanation:

      |
      |     |
|~~~~~|~~|~~|
|~|~~~|~~|~~|
|~|~|~|~~|~~|
-------------
4 2 0 3 2 5

Total trapped water = 9 units.

===========================================================
Approach 1: Prefix Max + Suffix Max Arrays
===========================================================

Intuition:
-----------
For every index i:

water[i] = min(maxLeft[i], maxRight[i]) - height[i]

where,

maxLeft[i]  = tallest bar from 0 to i
maxRight[i] = tallest bar from i to n-1

The water level above a bar is determined by the smaller
of the tallest bars on both sides.

Algorithm:
-----------
1. Build left_max array.
2. Build right_max array.
3. For every index:
      trapped_water += min(left_max[i], right_max[i]) - height[i]

Example:
---------
height = [4,2,0,3,2,5]

left_max:
[4,4,4,4,4,5]

right_max:
[5,5,5,5,5,5]

water:
[0,2,4,1,2,0]

Total = 9

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(n)

===========================================================
Approach 2: Optimal Two Pointer Solution
===========================================================

Intuition:
-----------
Instead of storing left_max and right_max arrays,
maintain only:

left pointer
right pointer
left_max
right_max

Observation:
------------
If left_max < right_max,

then water trapped at left depends only on left_max.

Reason:
--------
Since there exists a wall on the right that is taller
than left_max, the limiting factor becomes left_max.

Similarly,

if right_max <= left_max,

then water trapped at right depends only on right_max.

Algorithm:
-----------
1. Place pointers at both ends.
2. Update left_max and right_max.
3. Move the side having the smaller maximum.
4. Add trapped water.
5. Continue until pointers cross.

Example:
---------
height = [4,2,0,3,2,5]

left_max = 4
right_max = 5

Process left side:

water += 4 - 2 = 2
water += 4 - 0 = 4
water += 4 - 3 = 1
water += 4 - 2 = 2

Total = 9

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)

===========================================================
Recommended for Interviews
===========================================================

1. Explain Prefix/Suffix approach first.
2. Mention that it uses O(n) extra space.
3. Optimize to Two Pointers.
4. Explain:
   "The smaller maximum boundary determines the water level."

This is the solution generally expected in interviews.

===========================================================
Code
===========================================================
"""

from typing import List


# ---------------------------------------------------------
# Approach 1: Prefix Max + Suffix Max
# ---------------------------------------------------------
class SolutionPrefixSuffix:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0

        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water


# ---------------------------------------------------------
# Approach 2: Optimal Two Pointer
# ---------------------------------------------------------
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        left = 0
        right = n - 1

        left_max = 0
        right_max = 0

        water = 0

        while left <= right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:

                water += left_max - height[left]
                left += 1

            else:

                water += right_max - height[right]
                right -= 1

        return water


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------
if __name__ == "__main__":

    height = [4, 2, 0, 3, 2, 5]

    print("Prefix/Suffix Solution:")
    print(SolutionPrefixSuffix().trap(height))

    print("Two Pointer Solution:")
    print(Solution().trap(height))