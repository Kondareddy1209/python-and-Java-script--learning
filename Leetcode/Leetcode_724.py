"""
📌 Pivot Index (LeetCode 724) - GitHub Ready Notes

--------------------------------------------------
🧠 Problem Statement:
Given an integer array nums, return the pivot index.

A pivot index is an index where:
👉 Sum of all elements to the LEFT of the index
    equals
👉 Sum of all elements to the RIGHT of the index.

If no such index exists, return -1.

--------------------------------------------------
🚀 Approach: Prefix Sum / Running Sum

Instead of calculating left and right sums for every index
(which would take O(n²) time), we use:

1. total_sum = sum(nums)
2. left_sum = running sum of elements to the left

At each index i:

    right_sum = total_sum - left_sum - nums[i]

Why?

    total_sum = left_sum + nums[i] + right_sum

Rearranging:

    right_sum = total_sum - left_sum - nums[i]

If:

    left_sum == right_sum

then i is the pivot index.

--------------------------------------------------
✅ Dry Run

nums = [1, 7, 3, 6, 5, 6]

total_sum = 28
left_sum = 0

i = 0
left = 0
right = 28 - 0 - 1 = 27 ❌

i = 1
left = 1
right = 28 - 1 - 7 = 20 ❌

i = 2
left = 8
right = 28 - 8 - 3 = 17 ❌

i = 3
left = 11
right = 28 - 11 - 6 = 11 ✅

🎯 Pivot Index = 3

--------------------------------------------------
⏱️ Time Complexity:
O(n)
- Single traversal of the array

🧠 Space Complexity:
O(1)
- Only a few variables are used

--------------------------------------------------
⚠️ Common Mistakes:
❌ Updating left_sum before checking the condition
❌ Returning the pivot value instead of its index
❌ Forgetting to subtract nums[i] when computing right_sum
❌ Skipping the last index during iteration

--------------------------------------------------
🔥 Key Takeaways:
✔ Use total sum + running left sum
✔ Compute right sum in O(1)
✔ Check balance before updating left_sum
✔ Optimal solution runs in O(n) time

--------------------------------------------------
💻 Implementation
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate total sum of the array
        total_sum = sum(nums)

        # Running sum of elements to the left of current index
        left_sum = 0

        # Traverse each index and compare left and right sums
        for i in range(len(nums)):

            # Right sum = total sum - left sum - current element
            right_sum = total_sum - left_sum - nums[i]

            # If left and right sums are equal,
            # current index is the pivot index
            if left_sum == right_sum:
                return i

            # Update left sum for the next iteration
            left_sum += nums[i]

        # No pivot index found
        return -1