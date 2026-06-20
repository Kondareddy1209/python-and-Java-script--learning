"""
LeetCode 33. Search in Rotated Sorted Array
===========================================

Problem Statement
-----------------
There is an integer array `nums` sorted in ascending order
(with distinct values).

Before being passed to your function, nums is possibly rotated
at an unknown pivot index.

Example:

Original:
[0,1,2,4,5,6,7]

Rotated:
[4,5,6,7,0,1,2]

Given the array `nums` and an integer `target`,
return the index of target if it exists in nums,
otherwise return -1.

Examples
--------
Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4

------------------------------------------------

Input:
nums = [4,5,6,7,0,1,2]
target = 3

Output:
-1

------------------------------------------------

Input:
nums = [1]
target = 0

Output:
-1


Intuition
---------
A normal Binary Search works because the entire array
is sorted.

In a rotated sorted array:

[4,5,6,7,0,1,2]

the whole array is not sorted,
but at least one half is always sorted.

At every step:

1. Find mid.
2. Determine which half is sorted.
3. Check whether target lies inside that sorted half.
4. Discard the other half.

This allows us to reduce the search space by half
every iteration.

Approach
--------
Binary Search

Case 1:
Left Half Sorted

nums[l] <= nums[mid]

Example:

[4,5,6,7,0,1,2]
 l     m

If target lies between nums[l] and nums[mid],
search left.

Otherwise search right.

------------------------------------------------

Case 2:
Right Half Sorted

nums[mid] <= nums[r]

Example:

[4,5,6,7,0,1,2]
       m     r

If target lies between nums[mid] and nums[r],
search right.

Otherwise search left.

Time Complexity
---------------
O(log n)

Because every iteration cuts the search space in half.

Space Complexity
----------------
O(1)

Only a few variables are used.

"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            # Target Found
            if nums[mid] == target:
                return mid

            # Left Half Sorted
            if nums[mid] >= nums[l]:

                # Target lies in left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1

                # Search right half
                else:
                    l = mid + 1

            # Right Half Sorted
            else:

                # Target lies in right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                # Search left half
                else:
                    r = mid - 1

        return -1


# ============================================================
# Dry Run
# ============================================================

"""
Input:
nums = [4,5,6,7,0,1,2]
target = 0

------------------------------------------------

Initial

l = 0
r = 6

nums = [4,5,6,7,0,1,2]

------------------------------------------------

Iteration 1

mid = (0 + 6)//2
mid = 3

nums[mid] = 7

Target != 7

Check Sorted Half

nums[mid] >= nums[l]

7 >= 4

Left Half Sorted

[4,5,6,7]

Check if target lies here

4 <= 0 < 7

False

Search Right

l = mid + 1

l = 4

------------------------------------------------

Iteration 2

l = 4
r = 6

mid = (4 + 6)//2
mid = 5

nums[mid] = 1

Target != 1

nums[mid] >= nums[l]

1 >= 0

Left Half Sorted

[0,1]

Check

0 <= 0 < 1

True

Search Left

r = mid - 1

r = 4

------------------------------------------------

Iteration 3

l = 4
r = 4

mid = 4

nums[mid] = 0

Target Found

Return 4

------------------------------------------------

Output:
4
"""


# ============================================================
# Visualization
# ============================================================

"""
Example:

nums = [4,5,6,7,0,1,2]
target = 0

Step 1

[4,5,6,7,0,1,2]
 L     M     R

Left half sorted

Target not inside

Move Right

------------------------------------------------

[4,5,6,7,0,1,2]
         L M R

Left half sorted

Target inside

Move Left

------------------------------------------------

[4,5,6,7,0,1,2]
         M

Target Found

Answer = 4
"""


# ============================================================
# Why Does This Work?
# ============================================================

"""
Important Observation

A rotated sorted array always has at least one
sorted half.

Example:

[4,5,6,7,0,1,2]

Left Half:
[4,5,6,7]  -> Sorted

Right Half:
[0,1,2]    -> Sorted

At any position of mid:

Either

nums[l] <= nums[mid]

OR

nums[mid] <= nums[r]

One of them must be sorted.

Using this property,
we can decide where the target can exist
and eliminate half the search space.

Hence Binary Search still works.

"""


# ============================================================
# Edge Cases
# ============================================================

"""
1. Single Element

nums = [1]
target = 1

Output = 0

------------------------------------------------

2. Target Not Present

nums = [4,5,6,7,0,1,2]
target = 3

Output = -1

------------------------------------------------

3. Array Not Rotated

nums = [1,2,3,4,5]
target = 4

Output = 3

------------------------------------------------

4. Target at Pivot

nums = [4,5,6,7,0,1,2]
target = 0

Output = 4
"""


# ============================================================
# Example Usage
# ============================================================

if __name__ == "__main__":

    solution = Solution()

    print(solution.search([4,5,6,7,0,1,2], 0))
    print(solution.search([4,5,6,7,0,1,2], 3))
    print(solution.search([1], 0))