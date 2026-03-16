"""
Problem: Maximum Average Subarray I

Given an integer array nums and an integer k,
find the maximum average value of a subarray of length k.

Example
-------
nums = [1,12,-5,-6,50,3]
k = 4

Subarrays of size 4:

[1,12,-5,-6]  -> avg = 0.5
[12,-5,-6,50] -> avg = 12.75
[-5,-6,50,3]  -> avg = 10.5

Maximum average = 12.75


Concept Used
------------
Sliding Window Technique

Instead of recalculating the sum for every subarray,
we maintain a window of size k.

Steps:
1. Add the next element to the window
2. When window size == k → calculate result
3. Remove the leftmost element
4. Slide the window forward

Time Complexity  : O(n)
Space Complexity : O(1)


Sliding Window Visualization
----------------------------

nums = [1,12,-5,-6,50,3]
k = 4

Step 1

[1,12,-5,-6] 50 3
avg = 0.5


Step 2

1 [12,-5,-6,50] 3
avg = 12.75


Step 3

1 12 [-5,-6,50,3]
avg = 10.5


Maximum = 12.75
"""


class Solution:

    # ---------------------------------------------------------
    # APPROACH 1 : Sliding Window using FOR loop
    # ---------------------------------------------------------
    def findMaxAverage_for_loop(self, nums, k):
        """
        Uses a for loop with two pointers.

        l -> left pointer
        r -> right pointer

        r expands the window
        l shrinks the window
        """

        l = 0
        window_sum = 0
        max_avg = float('-inf')

        # r moves through the array
        for r in range(len(nums)):

            # Add new element entering the window
            window_sum += nums[r]

            # Check if window size reached k
            if r - l + 1 == k:

                # Calculate average
                current_avg = window_sum / k

                # Update maximum average
                max_avg = max(max_avg, current_avg)

                # Remove element leaving the window
                window_sum -= nums[l]

                # Move left pointer forward
                l += 1

        return max_avg

    # ---------------------------------------------------------
    # APPROACH 2 : Sliding Window using WHILE loop
    # ---------------------------------------------------------
    def findMaxAverage_while_loop(self, nums, k):
        """
        Same sliding window logic but implemented with a while loop.
        """

        l = 0
        r = 0
        window_sum = 0
        max_avg = float('-inf')

        # Continue until r reaches end of array
        while r < len(nums):

            # Add element at right pointer
            window_sum += nums[r]

            # If window size becomes k
            if r - l + 1 == k:

                # Calculate average
                current_avg = window_sum / k

                # Update max average
                max_avg = max(max_avg, current_avg)

                # Remove element leaving window
                window_sum -= nums[l]

                # Move left pointer
                l += 1

            # Move right pointer
            r += 1

        return max_avg


# ---------------------------------------------------------
# Example Test (for learning and debugging)
# ---------------------------------------------------------
if __name__ == "__main__":

    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    sol = Solution()

    print("FOR LOOP RESULT  :", sol.findMaxAverage_for_loop(nums, k))
    print("WHILE LOOP RESULT:", sol.findMaxAverage_while_loop(nums, k))