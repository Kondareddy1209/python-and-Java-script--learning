"""
Problem: Max Consecutive Ones III

Goal:
Given a binary array nums and an integer k,
return the maximum number of consecutive 1s
if you can flip at most k zeros.

---------------------------------------------------
🧠 HOW IT WORKS (Sliding Window Concept)
---------------------------------------------------

We maintain a window [l, r]:

1. Expand the window by moving 'r'
2. Count number of zeros in the window
3. If zeros > k → shrink window from left (move 'l')
4. Keep track of maximum window size

👉 Key idea:
We are allowed at most 'k' zeros inside the window.

---------------------------------------------------
"""

from typing import List
import time


# -------------------------------------------------
# Approach 1: While Loop (Manual pointer control)
# -------------------------------------------------
class SolutionWhile:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        count = 0   # number of zeros in window
        ans = 0

        while r < len(nums):
            # Step 1: Expand window
            if nums[r] == 0:
                count += 1

            # Step 2: Shrink window if invalid
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1

            # Step 3: Update answer
            ans = max(ans, r - l + 1)

            # Step 4: Move right pointer
            r += 1

        return ans


# -------------------------------------------------
# Approach 2: For Loop (Cleaner & Recommended)
# -------------------------------------------------
class SolutionFor:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        ans = 0

        for r in range(len(nums)):
            # Step 1: Expand window
            if nums[r] == 0:
                count += 1

            # Step 2: Shrink window if invalid
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1

            # Step 3: Update answer
            ans = max(ans, r - l + 1)

        return ans


# -------------------------------------------------
# Example + Runtime Measurement
# -------------------------------------------------
if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    # While Loop Approach
    start = time.time()
    result1 = SolutionWhile().longestOnes(nums, k)
    end = time.time()
    print("While Loop Result :", result1)
    print("Time Taken        :", (end - start) * 1000, "ms\n")

    # For Loop Approach
    start = time.time()
    result2 = SolutionFor().longestOnes(nums, k)
    end = time.time()
    print("For Loop Result   :", result2)
    print("Time Taken        :", (end - start) * 1000, "ms")


"""
---------------------------------------------------
⏱️ TIME COMPLEXITY
---------------------------------------------------
- Both approaches: O(n)
- Each element is visited at most twice (l and r)

---------------------------------------------------
💾 SPACE COMPLEXITY
---------------------------------------------------
- O(1) → no extra space used

---------------------------------------------------
⚡ NOTE ON RUNTIME (ms)
---------------------------------------------------
- Measured using time.time()
- Values depend on system performance
- Usually very small (few milliseconds)

---------------------------------------------------
🔥 FINAL TAKEAWAY
---------------------------------------------------
Sliding Window = Expand + Shrink + Track Answer

Master this → You can solve MANY problems!
---------------------------------------------------
"""