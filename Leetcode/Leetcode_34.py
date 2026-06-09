"""
LeetCode 34. Find First and Last Position of Element in Sorted Array

Problem:
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Approach:
Use Binary Search twice:

1. First Binary Search (Lower Bound)
   - Find the first index where target appears.
   - Move left when nums[mid] >= target.

2. Second Binary Search (Upper Bound)
   - Find the first index greater than target.
   - Move right when nums[mid] <= target.

3. If target does not exist, return [-1, -1].

4. Otherwise:
   - First occurrence = lower bound
   - Last occurrence = upper bound - 1

Example:
Input:  nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Time Complexity:
    O(log n)

Space Complexity:
    O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence (lower bound)
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        first = l

        # Check if target exists
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        # Find first index greater than target (upper bound)
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        last = l - 1

        return [first, last]


# Example Usage
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    sol = Solution()
    print(sol.searchRange(nums, target))  # Output: [3, 4]