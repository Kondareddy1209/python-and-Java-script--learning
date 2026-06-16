"""
=========================================================
53. Maximum Subarray - Brute Force Approach
=========================================================

Problem:
---------
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum,
and return its sum.

Example:
---------
Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the largest sum = 6.

---------------------------------------------------------
Brute Force Intuition:
---------------------------------------------------------
Generate all possible contiguous subarrays and calculate
their sums.

Keep track of the maximum sum encountered so far.

Instead of recalculating each subarray sum from scratch,
we maintain a running sum:

For every starting index i:
    Initialize current_sum = 0

    For every ending index j:
        Add nums[j] to current_sum
        Update max_sum

---------------------------------------------------------
Approach:
---------------------------------------------------------
1. Iterate through every possible starting index.
2. For each starting index:
      - Initialize current_sum = 0
3. Extend the subarray one element at a time.
4. Update the maximum subarray sum found so far.
5. Return max_sum.

---------------------------------------------------------
Dry Run:
---------------------------------------------------------
nums = [-2,1,-3,4,-1,2,1,-5,4]

i = 0
    [-2]                -> -2
    [-2,1]              -> -1
    [-2,1,-3]           -> -4
    ...

i = 3
    [4]                 -> 4
    [4,-1]              -> 3
    [4,-1,2]            -> 5
    [4,-1,2,1]          -> 6   <-- Maximum

Answer = 6

---------------------------------------------------------
Time Complexity:
---------------------------------------------------------
O(n²)

Outer loop runs n times.
Inner loop runs up to n times.

---------------------------------------------------------
Space Complexity:
---------------------------------------------------------
O(1)

Only a few extra variables are used.

=========================================================
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")

        for i in range(len(nums)):
            current_sum = 0

            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum