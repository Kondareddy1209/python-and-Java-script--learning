"""
LeetCode 724. Find Pivot Index

Problem:
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly
to the left of the index is equal to the sum of all the numbers strictly
to the right of the index.

If the index is on the left edge of the array, then the left sum is 0.
If the index is on the right edge of the array, then the right sum is 0.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3

Explanation:
Pivot index = 3
Left sum  = 1 + 7 + 3 = 11
Right sum = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1

Example 3:
Input: nums = [2,1,-1]
Output: 0

Approach (Brute Force):
For every index i:
1. Calculate the sum of elements to its left.
2. Calculate the sum of elements to its right.
3. If both sums are equal, return i.

Time Complexity:
- For each index, two sum() operations are performed.
- Each sum() can take O(n) time.
- Overall: O(n²)

Space Complexity:
- Slicing creates temporary arrays.
- Overall: O(n)
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i + 1:])

            if left == right:
                return i

        return -1


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 7, 3, 6, 5, 6]
    print(sol.pivotIndex(nums1))  # Output: 3

    nums2 = [1, 2, 3]
    print(sol.pivotIndex(nums2))  # Output: -1

    nums3 = [2, 1, -1]
    print(sol.pivotIndex(nums3))  # Output: 0