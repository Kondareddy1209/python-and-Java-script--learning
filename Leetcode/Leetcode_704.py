"""
Problem: Binary Search

Given a sorted array of integers and a target value, return the index of the target
if it exists. Otherwise, return -1.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Approach:
- Use Binary Search to reduce the search space by half each time.
- Compare the middle element with the target.
- Adjust the search range accordingly.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on a sorted array.

        :param nums: List[int] -> Sorted list of integers
        :param target: int -> Value to search
        :return: int -> Index of target if found, else -1
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right half
            elif nums[mid] < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        # Target not found
        return -1


# 🔹 Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))  # Output: -1