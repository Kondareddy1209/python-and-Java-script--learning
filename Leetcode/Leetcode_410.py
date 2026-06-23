"""
Problem: Split Array Largest Sum (LeetCode 410)

Given an integer array nums and an integer k, split nums into k non-empty
contiguous subarrays such that the largest sum among these subarrays is minimized.

Return the minimized largest subarray sum.

--------------------------------------------------

Example 1:

Input:
nums = [7, 2, 5, 10, 8]
k = 2

Output:
18

Explanation:

Split as:
[7, 2, 5] = 14
[10, 8]    = 18

Largest subarray sum = 18

No other split produces a smaller largest sum.

--------------------------------------------------

Example 2:

Input:
nums = [1, 2, 3, 4, 5]
k = 2

Output:
9

Explanation:

Split as:
[1, 2, 3] = 6
[4, 5]    = 9

Largest subarray sum = 9

--------------------------------------------------

Approach: Binary Search on Answer

Observation:

The answer lies between:

Minimum possible answer:
max(nums)

Reason:
Every element must belong to some subarray.
Therefore the largest subarray sum can never be smaller than
the largest element.

Maximum possible answer:
sum(nums)

Reason:
Put all elements into one subarray.

Search Space:

[max(nums), sum(nums)]

For each candidate answer (mid):

Check whether the array can be split into at most k subarrays
such that no subarray sum exceeds mid.

If possible:
    Try a smaller answer.
Else:
    Need a larger answer.

--------------------------------------------------

Time Complexity:

Binary Search:
O(log(sum(nums) - max(nums)))

Feasibility Check:
O(n)

Overall:
O(n * log(sum(nums)))

--------------------------------------------------

Space Complexity:

O(1)

--------------------------------------------------

Binary Search Pattern:

Minimum Valid Answer:

while left <= right:
    mid = left + (right - left) // 2

    if valid(mid):
        right = mid - 1
    else:
        left = mid + 1

return left

--------------------------------------------------
"""


from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Returns the minimum possible largest subarray sum.

        Args:
            nums (List[int]): Input array
            k (int): Number of subarrays

        Returns:
            int: Minimized largest subarray sum
        """

        # Optional safety check
        if k > len(nums):
            return -1

        left = max(nums)
        right = sum(nums)

        while left <= right:

            mid = left + (right - left) // 2

            if self.can_split(mid, nums, k):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_split(self, max_sum: int, nums: List[int], k: int) -> bool:
        """
        Checks if nums can be split into at most k subarrays
        where each subarray sum <= max_sum.

        Args:
            max_sum (int): Candidate answer
            nums (List[int]): Input array
            k (int): Number of subarrays

        Returns:
            bool
        """

        groups = 1
        current_sum = 0

        for num in nums:

            # Add current element to existing group
            if current_sum + num <= max_sum:
                current_sum += num

            # Create new group
            else:
                groups += 1
                current_sum = num

        return groups <= k


# --------------------------------------------------
# Driver Code
# --------------------------------------------------
if __name__ == "__main__":

    nums = [7, 2, 5, 10, 8]
    k = 2

    solution = Solution()

    answer = solution.splitArray(nums, k)

    print("Array:", nums)
    print("k:", k)
    print("Minimum Largest Subarray Sum:", answer)


"""
--------------------------------------------------
Dry Run
--------------------------------------------------

nums = [7, 2, 5, 10, 8]
k = 2

left  = max(nums) = 10
right = sum(nums) = 32

--------------------------------------------------

mid = 21

Groups:

[7,2,5] = 14
+10 => 24 > 21

Group 1 = 14

Group 2:
10 + 8 = 18

Total groups = 2

Valid

right = 20

--------------------------------------------------

mid = 15

Groups:

[7,2,5] = 14

Next:
10

Next:
8

Groups = 3

Invalid

left = 16

--------------------------------------------------

mid = 18

Groups:

[7,2,5] = 14

Next:
10 + 8 = 18

Groups = 2

Valid

right = 17

--------------------------------------------------

mid = 17

Groups:

[7,2,5] = 14

10

8

Groups = 3

Invalid

left = 18

--------------------------------------------------

left = 18
right = 17

Loop ends

Answer = 18

--------------------------------------------------

Visualization:

nums = [7, 2, 5, 10, 8]

Optimal Split:

[7, 2, 5] | [10, 8]

Subarray Sums:

14 | 18

Largest Sum = 18

Minimum Possible Answer = 18

--------------------------------------------------

Key Insight:

We are NOT searching for a position.

We are searching for the smallest valid answer.

Search Space:

[max(nums), sum(nums)]

This makes it a classic
"Binary Search on Answer" problem.
--------------------------------------------------
"""