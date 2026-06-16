"""
=========================================================
53. Maximum Subarray
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

=========================================================
Approach 1: Brute Force
=========================================================

Intuition:
----------
Generate all possible contiguous subarrays and calculate
their sums. Keep track of the maximum sum encountered.

Approach:
---------
1. Fix a starting index i.
2. Extend the subarray to every possible ending index j.
3. Maintain a running sum to avoid recomputing sums.
4. Update the maximum sum found so far.

Dry Run:
--------
nums = [-2,1,-3,4,-1,2,1,-5,4]

Starting at index 3:

[4]               -> 4
[4,-1]            -> 3
[4,-1,2]          -> 5
[4,-1,2,1]        -> 6   <-- Maximum

Time Complexity:
----------------
O(n²)

Outer loop runs n times.
Inner loop runs up to n times.

Space Complexity:
-----------------
O(1)

=========================================================
Approach 2: Kadane's Algorithm (Optimal)
=========================================================

Intuition:
----------
For every element, we have two choices:

1. Start a new subarray from the current element.
2. Extend the previous subarray.

Keep track of:
- curr : Maximum subarray sum ending at current index.
- maxi : Maximum subarray sum found so far.

Approach:
---------
Initialize:

curr = nums[0]
maxi = nums[0]

For every element:

curr = max(nums[i], curr + nums[i])

Update:

maxi = max(maxi, curr)

Return maxi.

Dry Run:
--------
nums = [-2,1,-3,4,-1,2,1,-5,4]

curr = -2
maxi = -2

1  -> curr = 1,  maxi = 1
-3 -> curr = -2, maxi = 1
4  -> curr = 4,  maxi = 4
-1 -> curr = 3,  maxi = 4
2  -> curr = 5,  maxi = 5
1  -> curr = 6,  maxi = 6
-5 -> curr = 1,  maxi = 6
4  -> curr = 5,  maxi = 6

Answer = 6

Time Complexity:
----------------
O(n)

Single traversal of the array.

Space Complexity:
-----------------
O(1)

Only two variables are used.

=========================================================
Comparison
=========================================================

Brute Force:
    Time  -> O(n²)
    Space -> O(1)

Kadane's Algorithm:
    Time  -> O(n)
    Space -> O(1)

Kadane's Algorithm is the optimal solution.
=========================================================
"""

from typing import List


class Solution:
    # ----------------------------------------------------
    # Approach 1: Brute Force
    # ----------------------------------------------------
    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        max_sum = float("-inf")

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum

    # ----------------------------------------------------
    # Approach 2: Kadane's Algorithm (Optimal)
    # ----------------------------------------------------
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])

            if curr > maxi:
                maxi = curr

        return maxi