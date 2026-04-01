from typing import List

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        """
        Problem:
        Given stock prices, find the maximum profit.
        You can buy and sell multiple times (but cannot hold multiple stocks).

        Approach Used:
        - Traverse the array
        - Add profit whenever there is an increase from previous day
        - This captures all upward trends (greedy approach)
        """

        # l → tracks the position of last minimum (not heavily used here)
        # profit → stores total profit
        l = 0
        profit = 0

        # Traverse from day 1 to end
        for r in range(1, len(nums)):

            # If current price is smaller, update buying point
            if nums[r] < nums[l]:
                l = r

            else:
                # If price increases from previous day, add profit
                if nums[r] > nums[r - 1]:
                    profit += nums[r] - nums[r - 1]

        return profit


"""
----------------------------------------
How It Works:
----------------------------------------
We capture every upward price movement.

Instead of finding one big profit,
we accumulate small profits:

Example:
[1, 5, 3, 6]

Profit = (5-1) + (6-3) = 4 + 3 = 7


----------------------------------------
Example 1:
----------------------------------------
nums = [7,1,5,3,6,4]

Steps:
1 → 5 → profit = 4
3 → 6 → profit = 3

Total Profit = 7


----------------------------------------
Example 2:
----------------------------------------
nums = [1,2,3,4,5]

Profit = (2-1) + (3-2) + (4-3) + (5-4) = 4


----------------------------------------
Example 3:
----------------------------------------
nums = [7,6,4,3,1]

No increasing sequence → Profit = 0


----------------------------------------
Time Complexity (T.C):
----------------------------------------
O(n) → single pass through array


----------------------------------------
Space Complexity (S.C):
----------------------------------------
O(1) → no extra space used


----------------------------------------
Notes:
----------------------------------------
- This is a greedy approach
- We sum all positive differences
- Equivalent to multiple buy-sell transactions
"""