"""
Problem: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be inserted
in order.

Example:
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Approach:
- Use Binary Search to efficiently find the position.
- If target is found, return its index.
- Otherwise, return the position where it can be inserted.
- At the end of the loop, 'left' pointer gives the correct insert position.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds the index of the target or the position where it should be inserted.

        :param nums: List[int] -> Sorted list of distinct integers
        :param target: int -> Target value to search
        :return: int -> Index of target or insert position
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search in the right half
            elif nums[mid] < target:
                left = mid + 1

            # Search in the left half
            else:
                right = mid - 1

        # Target not found, return insert position
        return left


# 🔹 Example usage (for local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # Output: 1