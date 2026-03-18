"""
Problem: Max Consecutive Ones III (LeetCode)

Goal:
Given a binary array nums and an integer k,
return the maximum number of consecutive 1s
if you can flip at most k zeros.

Concept:
Sliding Window Technique

---------------------------------------------------
Approach 1: While Loop (Manual right pointer)
---------------------------------------------------
"""

from typing import List


class SolutionWhile:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0          # left pointer
        r = 0          # right pointer
        count = 0      # number of zeros in current window
        ans = 0        # maximum length

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


"""
---------------------------------------------------
Approach 2: For Loop (Cleaner and Recommended)
---------------------------------------------------
"""


class SolutionFor:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0          # left pointer
        count = 0      # number of zeros in current window
        ans = 0        # maximum length

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


"""
---------------------------------------------------
Example Usage (for testing)
---------------------------------------------------
"""

if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    print("Using While Loop:", SolutionWhile().longestOnes(nums, k))
    print("Using For Loop  :", SolutionFor().longestOnes(nums, k))


"""
---------------------------------------------------
Key Takeaways:

1. Sliding window expands using 'r'
2. Shrinks using 'l' when condition breaks
3. Maintain constraint: count of zeros <= k
4. Time Complexity: O(n)
5. Space Complexity: O(1)

---------------------------------------------------
"""