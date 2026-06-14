"""
LeetCode 992. Subarrays with K Different Integers
-------------------------------------------------

Problem:
Given an integer array nums and an integer k, return the number of
good subarrays of nums.

A good subarray is a contiguous subarray that contains exactly k
distinct integers.

Example:
Input: nums = [1,2,1,2,3], k = 2
Output: 7

Approach:
----------
Instead of directly counting subarrays with exactly k distinct elements,
we use the following observation:

Exactly(k) = AtMost(k) - AtMost(k-1)

Why?

AtMost(k):
    Counts all subarrays having <= k distinct elements.

AtMost(k-1):
    Counts all subarrays having <= k-1 distinct elements.

When we subtract them, only the subarrays having exactly k distinct
elements remain.

-------------------------------------------------

Visualization:

Suppose:

nums = [1,2,1,2,3]
k = 2

AtMost(2) includes:
[1]
[1,2]
[1,2,1]
[1,2,1,2]
[2]
[2,1]
...
(all subarrays with <= 2 distinct numbers)

AtMost(1) includes:
[1]
[2]
[1]
[2]
[3]

Subtracting removes subarrays with only 1 distinct element,
leaving only those with exactly 2 distinct elements.

-------------------------------------------------

Sliding Window Idea for AtMost(k)
---------------------------------

Maintain:

l = left pointer
r = right pointer (loop variable)

freq = frequency map of elements in current window

Window always satisfies:

Number of distinct elements <= k

Whenever distinct elements become > k:
    shrink window from left

For every valid window:

[r]
[l........r]

All subarrays ending at r and starting between l and r are valid.

Count added:

r - l + 1

-------------------------------------------------

Example Dry Run
---------------

nums = [1,2,1]
k = 2

Step 1:
Window = [1]

Valid subarrays ending at index 0:
[1]

Count += 1

---------------------------------

Step 2:
Window = [1,2]

Valid subarrays ending at index 1:

[2]
[1,2]

Count += 2

---------------------------------

Step 3:
Window = [1,2,1]

Valid subarrays ending at index 2:

[1]
[2,1]
[1,2,1]

Count += 3

---------------------------------

Total AtMost(2) = 6

-------------------------------------------------

Why count += r - l + 1 ?
------------------------

Current valid window:

[l ........ r]

Every subarray ending at r is valid:

[r]
[r-1, r]
[r-2, r]
...
[l, ..., r]

Number of such subarrays:

r - l + 1

Example:

l = 2
r = 5

Possible subarrays ending at 5:

[5]
[4,5]
[3,4,5]
[2,3,4,5]

Count = 5 - 2 + 1 = 4

-------------------------------------------------

Code
-------------------------------------------------
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Exactly(k) = AtMost(k) - AtMost(k-1)
        """
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:
        """
        Returns number of subarrays having
        at most k distinct elements.
        """

        freq = defaultdict(int)

        left = 0
        count = 0

        for right in range(len(nums)):

            # Expand window
            freq[nums[right]] += 1

            # Shrink window if distinct count exceeds k
            while len(freq) > k:

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            # Number of valid subarrays ending at 'right'
            count += right - left + 1

        return count


"""
Complexity Analysis
-------------------

Let n = len(nums)

Time Complexity:
O(n)

Reason:
- Every element enters the window once.
- Every element leaves the window at most once.

Total pointer movement:
O(n)

Therefore:

AtMost(k)      -> O(n)
AtMost(k - 1)  -> O(n)

Overall:

O(n) + O(n)
= O(n)

-------------------------------------------------

Space Complexity:
O(k)

Reason:
Frequency map stores at most k distinct elements
inside the sliding window.

Worst Case:
O(n)

if all elements are distinct.

-------------------------------------------------

Key Interview Takeaways
-----------------------

1. Exact(k) is difficult to count directly.

2. Convert it into:

   Exact(k) = AtMost(k) - AtMost(k-1)

3. Use Sliding Window to efficiently compute AtMost(k).

4. For every valid window:

   count += window_size

   count += right - left + 1

5. This transforms an O(n²) problem into O(n).

-------------------------------------------------

Pattern Recognition
-------------------

Whenever you see:

"Exactly K"

Think:

Exactly(K)
=
AtMost(K)
-
AtMost(K-1)

This pattern is commonly used in:

1. Subarrays with K Distinct Integers
2. Binary Subarrays With Sum
3. Nice Subarrays
4. Subarrays with K Odd Numbers
5. Count of Substrings with K Distinct Characters

This is one of the most important Sliding Window patterns
for coding interviews.
"""