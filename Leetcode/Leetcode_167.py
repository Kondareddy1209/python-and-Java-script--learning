"""
Problem: Two Sum
---------------------------------
Given an array nums and a target,
return indices of two numbers such that:

nums[i] + nums[j] = target

---------------------------------
This file contains TWO approaches:

1. Two Pointer (only works for SORTED array)
2. HashMap (works for ANY array) ✅ Optimal

---------------------------------
"""

from typing import List


class Solution:

    # =========================================================
    # 🔹 APPROACH 1: TWO POINTER (SORTED ARRAY ONLY)
    # =========================================================
    def twoSum_two_pointer(self, nums: List[int], target: int) -> List[int]:
        """
        ⚠️ IMPORTANT:
        This works ONLY if the array is SORTED

        Step-by-step:
        1. Start with two pointers:
           l = 0 (start), r = n-1 (end)
        2. Calculate sum
        3. If sum == target → return indices
        4. If sum < target → move left pointer forward
        5. If sum > target → move right pointer backward
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]

            if s == target:
                return [l, r]  # 0-based indexing

            elif s < target:
                l += 1  # increase sum

            else:
                r -= 1  # decrease sum

        return [-1, -1]


    # =========================================================
    # 🔹 APPROACH 2: HASHMAP (OPTIMAL)
    # =========================================================
    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        Step-by-step:
        1. Create a hashmap to store value → index
        2. For each number:
            - Compute complement = target - current number
            - Check if complement exists in hashmap
        3. If yes → return indices
        4. Else → store current number
        """

        hashmap = {}

        for i, num in enumerate(nums):

            complement = target - num

            # Check if complement already exists
            if complement in hashmap:
                return [hashmap[complement], i]

            # Store current number
            hashmap[num] = i

        return [-1, -1]


# =========================================================
# 🧩 DRY RUN
# =========================================================
"""
Example:
nums = [2, 7, 11, 15]
target = 9

HashMap Approach:
-----------------
i = 0 → num = 2 → complement = 7 → not found → store {2:0}
i = 1 → num = 7 → complement = 2 → found → return [0,1]

Two Pointer (sorted):
---------------------
l = 0, r = 3 → 2 + 15 = 17 > 9 → r--
l = 0, r = 2 → 2 + 11 = 13 > 9 → r--
l = 0, r = 1 → 2 + 7 = 9 → return [0,1]
"""


# =========================================================
# ⏱️ TIME & SPACE COMPLEXITY
# =========================================================
"""
1. Two Pointer:
   --------------
   Time Complexity: O(n)
   Space Complexity: O(1)

   ⚠️ Only works if array is sorted


2. HashMap:
   ----------
   Time Complexity: O(n)
   Space Complexity: O(n)

   ✅ Works for unsorted arrays (BEST choice)
"""


# =========================================================
# 🔥 KEY TAKEAWAYS
# =========================================================
"""
👉 Two Pointer = only for sorted arrays
👉 HashMap = best for general case
👉 Avoid l <= r (use l < r)
👉 Don't return +1 unless problem asks 1-based index
"""


# =========================================================
# ✅ DRIVER CODE
# =========================================================
if __name__ == "__main__":
    sol = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    print("Two Pointer:", sol.twoSum_two_pointer(nums, target))
    print("HashMap:", sol.twoSum_hashmap(nums, target))