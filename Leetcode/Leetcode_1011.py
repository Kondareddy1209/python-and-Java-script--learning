"""
LeetCode 1011. Capacity To Ship Packages Within D Days

Problem:
Given an array of package weights and an integer days,
return the least weight capacity of the ship that will
result in all the packages being shipped within the given days.

Approach:
Binary Search on Answer

Search Space:
- Minimum capacity = max(weights)
  (because the ship must be able to carry the heaviest package)

- Maximum capacity = sum(weights)
  (because the ship can carry all packages in one day)

For each candidate capacity (mid):
- Calculate how many days are required to ship all packages.
- If required days <= given days:
    Capacity works, try a smaller capacity.
- Otherwise:
    Capacity is too small, try a larger capacity.

Time Complexity:
O(n * log(sum(weights)))

Space Complexity:
O(1)
"""


class Solution:
    def shipWithinDays(self, weights, days):
        # Minimum possible capacity
        left = max(weights)

        # Maximum possible capacity
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2

            required_days = self.findDays(weights, mid)

            # Capacity is sufficient
            if required_days <= days:
                right = mid - 1

            # Capacity is too small
            else:
                left = mid + 1

        # First valid minimum capacity
        return left

    def findDays(self, weights, capacity):
        days = 1
        current_load = 0

        for weight in weights:

            # Package doesn't fit in current day
            if current_load + weight > capacity:
                days += 1
                current_load = weight

            # Package fits in current day
            else:
                current_load += weight

        return days


# Example Usage
if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    solution = Solution()
    answer = solution.shipWithinDays(weights, days)

    print("Minimum Ship Capacity:", answer)

"""
Output:
Minimum Ship Capacity: 15
"""