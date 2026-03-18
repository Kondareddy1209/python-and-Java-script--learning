"""
Problem: Product of Array Except Self

Goal:
Given an integer array nums, return an array answer such that:
answer[i] = product of all elements except nums[i]

⚠️ Constraint:
- Do NOT use division
- Must run in O(n)

---------------------------------------------------
🧠 HOW IT WORKS (Prefix + Postfix Concept)
---------------------------------------------------

Instead of division, we use two passes:

👉 Prefix pass:
For each index i, store product of all elements BEFORE i

👉 Postfix pass:
Multiply with product of all elements AFTER i

Example:
nums = [1, 2, 3, 4]

Prefix:
[1, 1, 2, 6]

Postfix:
[24, 12, 4, 1]

Final Answer:
[24, 12, 8, 6]

---------------------------------------------------
"""

from typing import List
import time


# -------------------------------------------------
# Approach 1: Prefix + Postfix (Optimal)
# -------------------------------------------------
class SolutionOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Prefix pass
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Postfix pass
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


# -------------------------------------------------
# Approach 2: Brute Force (for understanding only)
# -------------------------------------------------
class SolutionBrute:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            result.append(prod)

        return result


# -------------------------------------------------
# Example + Runtime Measurement
# -------------------------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    # Optimal Approach
    start = time.time()
    result1 = SolutionOptimal().productExceptSelf(nums)
    end = time.time()
    print("Optimal Result :", result1)
    print("Time Taken     :", (end - start) * 1000, "ms\n")

    # Brute Force Approach
    start = time.time()
    result2 = SolutionBrute().productExceptSelf(nums)
    end = time.time()
    print("Brute Result   :", result2)
    print("Time Taken     :", (end - start) * 1000, "ms")


"""
---------------------------------------------------
⏱️ TIME COMPLEXITY
---------------------------------------------------

Optimal Approach:
- O(n) → two passes

Brute Force:
- O(n^2) → nested loops

---------------------------------------------------
💾 SPACE COMPLEXITY
---------------------------------------------------

Optimal:
- O(1) extra space (excluding output array)

Brute:
- O(1)

---------------------------------------------------
⚡ NOTE ON RUNTIME (ms)
---------------------------------------------------
- Measured using time.time()
- Depends on system performance
- Optimal is MUCH faster than brute

---------------------------------------------------
🔥 FINAL TAKEAWAY
---------------------------------------------------

Prefix + Postfix Pattern = No division needed

Used in:
- Product problems
- Range queries
- Accumulation problems

---------------------------------------------------
"""