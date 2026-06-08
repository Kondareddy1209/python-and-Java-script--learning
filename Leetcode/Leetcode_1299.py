# LeetCode 1299. Replace Elements with Greatest Element on Right Side
#
# Problem Statement:
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with -1.
#
# Return the resulting array.
#
# Example:
# Input:  arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
# Approach:
# 1. Traverse the array from right to left.
# 2. Maintain a variable `max_right` representing the maximum element seen so far.
# 3. Build a suffix maximum array (`right`) where each position stores the
#    greatest element from that index to the end.
# 4. Reverse the suffix array to restore the original order.
# 5. Since each element must be replaced by the greatest element strictly
#    to its right:
#       - Remove the first element of the suffix maximum array.
#       - Append -1 for the last position.
#
# Example Walkthrough:
# arr = [17,18,5,4,6,1]
#
# Suffix maximums while traversing from right:
# [1,6,6,6,18,18]
#
# After reversing:
# [18,18,6,6,6,1]
#
# Shift left and append -1:
# [18,6,6,6,1,-1]
#
# Time Complexity: O(n)
# - Single traversal to build suffix maximums.
# - Reverse operation takes O(n).
# - Final slicing operation takes O(n).
#
# Space Complexity: O(n)
# - Additional suffix maximum array is used.

from typing import List

class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return [-1]

        right = []
        max_right = 0

        # Build suffix maximum array
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_right:
                right.append(nums[i])
                max_right = nums[i]
            else:
                right.append(max_right)

        # Restore original order
        right.reverse()

        # Replace each element with the greatest element to its right
        return right[1:] + [-1]