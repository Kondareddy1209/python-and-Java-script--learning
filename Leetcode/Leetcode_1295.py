"""
📌 Problem: Find Numbers with Even Number of Digits

Given an array of integers `nums`, return how many of them contain
an even number of digits.

------------------------------------------------------------
🧠 Approach:
1. Traverse each number in the array.
2. Convert the number to string (or calculate digits mathematically).
3. Count digits using len(str(num)).
4. If the number of digits is even, increment the counter.
5. Return the final count.

------------------------------------------------------------
⚡ Time Complexity (T.C): O(n * d)
- n = number of elements
- d = number of digits (conversion to string)

👉 Practically treated as O(n)

------------------------------------------------------------
💾 Space Complexity (S.C): O(1)
- No extra space used except variables

------------------------------------------------------------
🔄 Commit History:

✔ Commit v1:
- Basic implementation using loop and string conversion

✔ Commit v2:
- Improved readability using direct iteration instead of indexing

✔ Commit v3:
- Optimized to one-liner using generator expression

✔ Commit v4:
- Alternative math-based solution (without string conversion)

------------------------------------------------------------
"""

from typing import List
import math


class Solution:

    # ✅ Commit v1 (Basic Solution)
    def findNumbers_v1(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count


    # ✅ Commit v2 (Improved Readability)
    def findNumbers_v2(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


    # ✅ Commit v3 (Pythonic One-liner)
    def findNumbers_v3(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


    # ✅ Commit v4 (Math-Based Optimization)
    def findNumbers_v4(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digits = int(math.log10(num)) + 1
            if digits % 2 == 0:
                count += 1
        return count


"""
📌 Example:

Input: nums = [12, 345, 2, 6, 7896]
Output: 2

Explanation:
- 12 → 2 digits (even) ✅
- 345 → 3 digits ❌
- 2 → 1 digit ❌
- 6 → 1 digit ❌
- 7896 → 4 digits (even) ✅

So, output = 2
"""