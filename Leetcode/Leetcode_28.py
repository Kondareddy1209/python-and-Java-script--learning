"""
Problem: Implement strStr()
---------------------------------
Given two strings:
- haystack (main string)
- needle (pattern)

Return the index of the first occurrence of needle in haystack.
If not found, return -1.

---------------------------------
This file contains TWO approaches:

1. Manual Brute Force (Character-by-character comparison)
2. Python Slicing (Shortcut approach)

---------------------------------
"""


class Solution:
    # =========================================================
    # 🔹 APPROACH 1: MANUAL BRUTE FORCE (CHARACTER MATCHING)
    # =========================================================
    def strStr_bruteforce(self, haystack: str, needle: str) -> int:
        """
        Step-by-step logic:

        1. Get lengths of both strings
        2. Edge case: if needle is empty → return 0
        3. Loop through each possible starting index
        4. Compare characters one by one
        5. If full match → return index
        6. If no match → return -1
        """

        n = len(haystack)
        m = len(needle)

        # Edge case
        if m == 0:
            return 0

        # Loop through possible starting points
        for i in range(n - m + 1):

            j = 0  # pointer for needle

            # Compare characters one by one
            for k in range(m):

                # Compare current characters
                if haystack[i + k] == needle[j]:
                    j += 1
                else:
                    break  # mismatch → stop checking

            # If all characters matched
            if j == m:
                return i

        return -1


    # =========================================================
    # 🔹 APPROACH 2: PYTHON SLICING (SHORTCUT)
    # =========================================================
    def strStr_slicing(self, haystack: str, needle: str) -> int:
        """
        Step-by-step logic:

        1. Get lengths of both strings
        2. Edge case: if needle is empty → return 0
        3. Slide a window of size m over haystack
        4. Compare substring directly using slicing
        5. If match → return index
        6. If no match → return -1
        """

        n = len(haystack)
        m = len(needle)

        # Edge case
        if m == 0:
            return 0

        # Slide window
        for i in range(n - m + 1):

            # Extract substring and compare
            if haystack[i:i + m] == needle:
                return i

        return -1


# =========================================================
# 🧩 HOW IT WORKS (DRY RUN)
# =========================================================
"""
Example:
haystack = "sadbutsad"
needle   = "sad"

Brute Force:
------------
i = 0 → compare "sad" → match → return 0

Slicing:
--------
i = 0 → haystack[0:3] = "sad" → match → return 0
"""


# =========================================================
# ⏱️ TIME & SPACE COMPLEXITY
# =========================================================
"""
1. Brute Force Approach:
   ----------------------
   Time Complexity: O(n * m)
   - For each index, we compare up to m characters

   Space Complexity: O(1)
   - No extra space used


2. Slicing Approach:
   ------------------
   Time Complexity: O(n * m)
   - Slicing takes O(m) and happens n times

   Space Complexity: O(m)
   - Substring slice creates a new string


# =========================================================
# 🔥 KEY DIFFERENCE
# =========================================================
Brute Force:
- More control
- No extra memory
- Slightly more interview-friendly

Slicing:
- Cleaner and shorter
- Pythonic
- Uses extra space


# =========================================================
# 🚀 FINAL TAKEAWAY
# =========================================================
👉 Both approaches use "Sliding Window"
👉 Brute Force = Manual comparison
👉 Slicing = Shortcut using Python features
👉 For optimal solution → use KMP (O(n + m))
"""


# =========================================================
# ✅ DRIVER CODE (for local testing)
# =========================================================
if __name__ == "__main__":
    sol = Solution()

    haystack = "sadbutsad"
    needle = "sad"

    print("Brute Force Result:", sol.strStr_bruteforce(haystack, needle))
    print("Slicing Result:", sol.strStr_slicing(haystack, needle))