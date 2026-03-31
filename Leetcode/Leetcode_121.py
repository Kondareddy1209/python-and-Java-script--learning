"""
LeetCode Problem: 121. Best Time to Buy and Sell Stock

Problem Statement:
You are given an array 'prices' where prices[i] is the price of a stock on day i.
You want to maximize your profit by choosing:
- one day to buy
- one different day in the future to sell

Return the maximum profit you can achieve.
If no profit is possible, return 0.

--------------------------------------------------

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation:
Buy at price = 1 (day 2)
Sell at price = 6 (day 5)
Profit = 6 - 1 = 5

--------------------------------------------------

Approach (Two Pointer / Sliding Window Idea):

- Use two pointers:
  l → represents the buying day (minimum price so far)
  r → represents the selling day (current day)

- Traverse the array:
  1. If current price is lower than the buying price:
     → update buying day (l = r)
  2. Else:
     → calculate profit = prices[r] - prices[l]
     → update maximum profit

--------------------------------------------------

Dry Run:

prices = [7,1,5,3,6,4]

Step-by-step:
l = 0 (price = 7)

r = 1 → price = 1 → update l = 1
r = 2 → price = 5 → profit = 5 - 1 = 4 → max = 4
r = 3 → price = 3 → profit = 3 - 1 = 2 → max = 4
r = 4 → price = 6 → profit = 6 - 1 = 5 → max = 5
r = 5 → price = 4 → profit = 4 - 1 = 3 → max = 5

Final Answer = 5

--------------------------------------------------

Time Complexity:
O(n) → We traverse the array once

Space Complexity:
O(1) → No extra space used

--------------------------------------------------

Key Learnings:
- Use two-pointer technique for optimization
- Always track minimum value dynamically
- Avoid brute force (O(n^2))
- This pattern is common in many array problems

--------------------------------------------------
"""


from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        # l → pointer to track minimum price (buy day)
        # m → stores maximum profit
        l = 0
        m = 0

        # r → pointer to traverse array (sell day)
        for r in range(1, len(nums)):

            # If current price is lower than buying price
            # update buying day
            if nums[l] > nums[r]:
                l = r

            else:
                # Calculate profit
                new = nums[r] - nums[l]

                # Update maximum profit
                m = max(new, m)

        # Return final maximum profit
        return m


# ------------------------------
# Example Run (for testing)
# ------------------------------
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print("Maximum Profit:", sol.maxProfit(prices))