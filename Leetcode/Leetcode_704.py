\# LeetCode 704. Binary Search
#
# Approach:
# - Initialize two pointers:
#     left = 0
#     right = last index of the array
# - Find the middle element.
# - If the middle element is the target, return its index.
# - If the target is greater than the middle element,
#   search in the right half.
# - Otherwise, search in the left half.
# - Repeat until the search space becomes empty.
#
# Time Complexity: O(log n)
# - The search space is reduced to half in every iteration.
#
# Space Complexity: O(1)
# - Only constant extra space is used.
#
# Step-by-Step Execution (Example)
# ---------------------------------
# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
#
# Initial:
# left = 0
# right = 5
#
# Iteration 1:
# mid = 0 + (5 - 0) // 2 = 2
# nums[mid] = 3
# 3 < 9
# Move left to mid + 1
#
# left = 3
# right = 5
#
# Iteration 2:
# mid = 3 + (5 - 3) // 2 = 4
# nums[mid] = 9
# Target found.
#
# Return 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1