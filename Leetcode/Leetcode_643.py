"""
Problem: Maximum Average Subarray I

Given an integer array nums and an integer k,
find the maximum average value of a subarray of length k.

Example:
nums = [1,12,-5,-6,50,3]
k = 4

Subarrays of length 4:
[1,12,-5,-6]  -> average = 0.5
[12,-5,-6,50] -> average = 12.75
[-5,-6,50,3]  -> average = 10.5

Maximum average = 12.75

Concept Used:
Sliding Window Technique

Instead of recalculating the sum of every subarray,
we maintain a moving window of size k.

Steps:
1. Add the next element to the window
2. Calculate average when window size reaches k
3. Remove the leftmost element
4. Slide the window forward

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    # ------------------------------------------------------------
    # Approach 1: Sliding Window using FOR loop
    # ------------------------------------------------------------
    def findMaxAverage_for_loop(self, nums, k):
        """
        This method uses a for loop with two pointers.
        r -> right pointer (expands window)
        l -> left pointer (shrinks window)
        """

        l = 0                      # left pointer
        window_sum = 0             # stores current window sum
        max_avg = float('-inf')    # stores maximum average found

        # r represents the right pointer of the sliding window
        for r in range(len(nums)):

            # Step 1: Add the new element to the window
            window_sum += nums[r]

            # Step 2: Check if window size becomes k
            if (r - l + 1) == k:

                # Step 3: Compute average of current window
                current_avg = window_sum / k

                # Update maximum average
                max_avg = max(max_avg, current_avg)

                # Step 4: Remove the leftmost element
                window_sum -= nums[l]

                # Step 5: Move the left pointer forward
                l += 1

        return max_avg

    # ------------------------------------------------------------
    # Approach 2: Sliding Window using WHILE loop
    # ------------------------------------------------------------
    def findMaxAverage_while_loop(self, nums, k):
        """
        This method uses a while loop instead of a for loop.
        The logic remains exactly the same.
        """

        l = 0                       # left pointer
        r = 0                       # right pointer
        window_sum = 0              # sum of elements inside window
        max_avg = float('-inf')     # track maximum average

        # Continue until right pointer reaches the end
        while r < len(nums):

            # Step 1: Add element at right pointer
            window_sum += nums[r]

            # Step 2: Check if window size becomes k
            if (r - l + 1) == k:

                # Calculate current average
                current_avg = window_sum / k

                # Update maximum average
                max_avg = max(max_avg, current_avg)

                # Step 3: Remove the leftmost element
                window_sum -= nums[l]

                # Step 4: Move left pointer forward
                l += 1

            # Step 5: Move right pointer forward
            r += 1

        return max_avg


# ------------------------------------------------------------
# Example Test (for understanding / local testing)
# ------------------------------------------------------------
if __name__ == "__main__":

    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    sol = Solution()

    print("Using FOR loop:", sol.findMaxAverage_for_loop(nums, k))
    print("Using WHILE loop:", sol.findMaxAverage_while_loop(nums, k))