"""
📌 Pivot Index (LeetCode 724) - GitHub Ready Notes

Author: Your Name

--------------------------------------------------
🧠 Problem Statement:
Given an integer array nums, return the pivot index.

The pivot index is the index where:
👉 Sum of elements on the LEFT == Sum of elements on the RIGHT

If no such index exists, return -1.

--------------------------------------------------
🚀 Approach: Prefix Sum Technique

Instead of recalculating left and right sums every time (which is slow),
we use a running sum (prefix sum).

Key Idea:
- total_sum = sum of all elements
- left_sum = keeps increasing as we iterate

At any index i:
Right sum = total_sum - left_sum - nums[i]

Condition:
👉 left_sum == total_sum - left_sum - nums[i]

--------------------------------------------------
✅ Step-by-Step Dry Run

Example:
nums = [1, 7, 3, 6, 5, 6]

Step 1:
total_sum = 28
left_sum = 0

Index 0:
left = 0
right = 28 - 0 - 1 = 27 ❌

Index 1:
left = 1
right = 28 - 1 - 7 = 20 ❌

Index 2:
left = 8
right = 28 - 8 - 3 = 17 ❌

Index 3:
left = 11
right = 28 - 11 - 6 = 11 ✅

🎯 Pivot Index = 3

--------------------------------------------------
💻 Implementation
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        # ✅ Using FOR loop (recommended)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1


# ---------------------------------------------
# ✅ Alternative: Using WHILE loop
# ---------------------------------------------

class SolutionWhile:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        i = 0

        while i < len(nums):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
            i += 1

        return -1


"""
--------------------------------------------------
⏱️ Time Complexity:
O(n)
- We traverse the array once

🧠 Space Complexity:
O(1)
- No extra space used (only variables)

--------------------------------------------------
⚠️ Common Mistakes:
❌ Removing duplicates (changes positions)
❌ Returning value instead of index
❌ Including current element in left sum before checking
❌ Wrong loop condition (like while i > len(nums))

--------------------------------------------------
🔥 Key Takeaways:
✔ Always preserve array structure
✔ Use prefix sum for efficiency
✔ Think in terms of LEFT and RIGHT balance


"""
