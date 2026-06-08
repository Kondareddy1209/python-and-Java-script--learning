# LeetCode 2149. Rearrange Array Elements by Sign
#
# Problem Statement:
# Given an array nums of even length consisting of an equal number of positive
# and negative integers, rearrange the elements such that:
#
# 1. Every consecutive pair of integers has opposite signs.
# 2. For all integers with the same sign, their relative order is preserved.
# 3. The rearranged array begins with a positive integer.
#
# Return the modified array.
#
# Example:
# Input:  nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
#
# Approach:
# - Create a result array of the same size as nums.
# - Use two pointers:
#     pos = 0 -> stores the next available even index for positive numbers.
#     neg = 1 -> stores the next available odd index for negative numbers.
# - Traverse the input array once:
#     * If the current number is positive, place it at index 'pos'
#       and move pos by 2.
#     * If the current number is negative, place it at index 'neg'
#       and move neg by 2.
# - This preserves the relative ordering of positive and negative numbers
#   while ensuring alternating signs.
#
# Time Complexity: O(n)
# - Each element is visited exactly once.
#
# Space Complexity: O(n)
# - An additional array of size n is used to store the result.

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Even indices for positive numbers
        pos = 0

        # Odd indices for negative numbers
        neg = 1

        # Result array
        temp = [0] * n

        for i in range(n):
            if nums[i] > 0:
                temp[pos] = nums[i]
                pos += 2
            else:
                temp[neg] = nums[i]
                neg += 2

        return temp