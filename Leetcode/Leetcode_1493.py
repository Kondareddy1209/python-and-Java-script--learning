"""
Problem: Longest Subarray of 1's After Deleting One Element

Approach: Sliding Window

We maintain a window that contains at most ONE zero.
Why? Because we are allowed to delete one element.

So if the window has:
- 0 zeros → all 1's → we must delete one → length = window_size - 1
- 1 zero → delete that zero → remaining all 1's

Hence, answer = r - l
"""

class Solution:
    # ----------------------------------------
    # VERSION 1: Using WHILE loop
    # ----------------------------------------
    def longestSubarray_while(self, nums):
        l = 0
        r = 0
        count_0 = 0  # count of zeros in window
        ans = 0

        while r < len(nums):
            # Step 1: Expand window
            if nums[r] == 0:
                count_0 += 1

            # Step 2: Shrink window if more than 1 zero
            while count_0 > 1:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            # Step 3: Update answer
            # r - l instead of (r - l + 1) because we must delete one element
            ans = max(ans, r - l)

            r += 1

        return ans

    # ----------------------------------------
    # VERSION 2: Using FOR loop (Recommended)
    # ----------------------------------------
    def longestSubarray_for(self, nums):
        l = 0
        count_0 = 0
        ans = 0

        for r in range(len(nums)):
            # Step 1: Expand window
            if nums[r] == 0:
                count_0 += 1

            # Step 2: Shrink window if more than 1 zero
            while count_0 > 1:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            # Step 3: Update answer
            ans = max(ans, r - l)

        return ans


# ----------------------------------------
# 🔍 Example Usage (for testing locally)
# ----------------------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 0, 1]

    print("While Loop Version:", sol.longestSubarray_while(nums))
    print("For Loop Version:", sol.longestSubarray_for(nums))