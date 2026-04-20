"""
Problem: House Robber

You are given an integer array `nums` where each element represents the amount
of money in a house. Adjacent houses cannot be robbed (security alarm).

Goal:
Return the maximum amount of money you can rob without robbing two adjacent houses.

Example:
Input: nums = [6, 7, 1, 3, 8, 2, 4]
Output: 19

Approach:
We use Dynamic Programming with space optimization.

At each house, we decide:
1. Rob current house → add current value + money from house i-2
2. Skip current house → take money from previous house

Transition:
curr = max(nums[i] + prev2, prev1)

Where:
prev1 = max money till previous house (i-1)
prev2 = max money till house before previous (i-2)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  # max money till previous house
        prev2 = 0  # max money till house before previous

        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    nums = [6, 7, 1, 3, 8, 2, 4]
    sol = Solution()
    print("Maximum money that can be robbed:", sol.rob(nums))