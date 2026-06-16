"""
=========================================================
152. Maximum Product Subarray
=========================================================

Problem:
---------
Given an integer array nums, find a contiguous non-empty
subarray within the array that has the largest product,
and return the product.

Example:
---------
Input:
nums = [2, 3, -2, 4]

Output:
6

Explanation:
[2, 3] has the largest product = 6

=========================================================
Approach 1: Brute Force
=========================================================

Intuition:
----------
Generate all possible contiguous subarrays and calculate
their products.

Instead of recomputing the product for every subarray from
scratch, maintain a running product while extending the
subarray.

Approach:
---------
1. Fix a starting index i.
2. Initialize product = 1.
3. Extend the subarray one element at a time.
4. Update the running product.
5. Update the maximum product found so far.

Dry Run:
--------
nums = [2, -5, -2, -4, 3]

i = 0
[2]                  -> 2
[2,-5]               -> -10
[2,-5,-2]            -> 20
[2,-5,-2,-4]         -> -80
[2,-5,-2,-4,3]       -> -240

i = 1
[-5]                 -> -5
[-5,-2]              -> 10
[-5,-2,-4]           -> -40
[-5,-2,-4,3]         -> -120

i = 2
[-2]                 -> -2
[-2,-4]              -> 8
[-2,-4,3]            -> 24   <-- Maximum Product

Answer = 24

Time Complexity:
----------------
O(n²)

Space Complexity:
-----------------
O(1)

=========================================================
Approach 2: Prefix & Suffix Scan (Optimal)
=========================================================

Intuition:
----------
Negative numbers can flip the sign of a product.

Positive × Negative = Negative
Negative × Negative = Positive

If the array contains an odd number of negative values,
the maximum product can be obtained by excluding:

1. Elements before the first negative, or
2. Elements after the last negative.

To cover both possibilities:

- Scan from Left → Right (Prefix Product)
- Scan from Right → Left (Suffix Product)

Keep track of the maximum product encountered.

Handling Zero:
--------------
A zero breaks the product chain.

Example:

nums = [2, 3, 0, 4, 5]

After multiplying by zero:

prefix = 0

All future products remain zero.

Therefore:

if prefix == 0:
    prefix = 1

Similarly for suffix.

Dry Run:
--------
nums = [2, -5, -2, -4, 3]

i = 0
prefix = 2
suffix = 3
maxi   = 3

i = 1
prefix = -10
suffix = -12
maxi   = 3

i = 2
prefix = 20
suffix = 24
maxi   = 24

i = 3
prefix = -80
suffix = -120
maxi   = 24

i = 4
prefix = -240
suffix = -240
maxi   = 24

Answer = 24

Maximum Product Subarray:

[-2, -4, 3]

Product:

(-2) × (-4) × 3 = 24

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)

=========================================================
Comparison
=========================================================

Brute Force:
    Time  -> O(n²)
    Space -> O(1)

Prefix & Suffix:
    Time  -> O(n)
    Space -> O(1)

The Prefix & Suffix approach is the optimal solution.

=========================================================
"""

from typing import List


class Solution:

    # =====================================================
    # Approach 1: Brute Force
    # =====================================================
    def maxProductBruteForce(self, nums: List[int]) -> int:
        maxi = float("-inf")

        for i in range(len(nums)):
            curr = 1

            for j in range(i, len(nums)):
                curr *= nums[j]
                maxi = max(maxi, curr)

        return maxi

    # =====================================================
    # Approach 2: Prefix & Suffix Scan (Optimal)
    # =====================================================
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxi = float("-inf")

        n = len(nums)

        for i in range(n):

            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            maxi = max(maxi, prefix, suffix)

        return maxi