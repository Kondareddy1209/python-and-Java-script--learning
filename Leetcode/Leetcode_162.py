"""
# 162. Find Peak Element

## Problem Statement

A peak element is an element that is **strictly greater than its neighbors**.

Given a 0-indexed integer array `nums`, find a peak element and return its index.
If the array contains multiple peaks, return the index of **any** peak.

You may imagine that:

nums[-1] = nums[n] = -∞

This means the elements outside the array are considered negative infinity.

### Example 1
Input:
nums = [1,2,3,1]

Output:
2

Explanation:
nums[2] = 3 is greater than both neighbors.

### Example 2
Input:
nums = [1,2,1,3,5,6,4]

Output:
5

Explanation:
nums[5] = 6 is a peak element.

---

## Intuition

A linear scan can find a peak in O(n) time, but the problem asks for an
algorithm with O(log n) complexity.

We can use **Binary Search** by observing the slope around the middle element.

Consider:

nums[mid] and nums[mid + 1]

### Case 1:
nums[mid] > nums[mid + 1]

This means we are on a descending slope.

Example:
1 3 5 4 2

      mid

Since the sequence is decreasing after `mid`, a peak must exist on the
left side (including `mid` itself).

Therefore:
r = mid

### Case 2:
nums[mid] < nums[mid + 1]

This means we are on an ascending slope.

Example:
1 2 4 6 8

      mid

Since the sequence is increasing, a peak must exist on the
right side.

Therefore:
l = mid + 1

By repeatedly reducing the search space, we eventually reach a single
element which is guaranteed to be a peak.

---

## Approach

1. Initialize:
   - l = 0
   - r = n - 1

2. While l < r:
   - Find middle index.
   - Compare nums[mid] and nums[mid + 1].

3. If nums[mid] > nums[mid + 1]:
   - Peak lies on the left side.
   - Move r = mid.

4. Else:
   - Peak lies on the right side.
   - Move l = mid + 1.

5. When l == r, that index is the peak.

---

## Dry Run

nums = [1,2,3,1]

Initial:
l = 0, r = 3

mid = 1
nums[1] = 2
nums[2] = 3

2 < 3
=> Peak is on right side

l = 2

Now:
l = 2, r = 3

mid = 2
nums[2] = 3
nums[3] = 1

3 > 1
=> Peak is on left side (including mid)

r = 2

Now:
l = r = 2

Return 2

---

## Why Binary Search Works?

Whenever we compare nums[mid] and nums[mid + 1]:

- If the slope goes down, a peak exists on the left side.
- If the slope goes up, a peak exists on the right side.

Since one half can always be discarded, binary search is applicable.

The search space reduces by half in every iteration.

---

## Time Complexity

Binary search halves the search space in every iteration.

Time Complexity: O(log n)

---

## Space Complexity

Only a few variables are used.

Space Complexity: O(1)

---

## LeetCode Solution
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l