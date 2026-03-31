"""
LeetCode Problem: 88. Merge Sorted Array

Problem Statement:
You are given two sorted integer arrays nums1 and nums2, and two integers m and n.

- nums1 has a size of m + n, where:
  - first m elements are valid
  - last n elements are 0 (empty space)

- nums2 has n elements

Merge nums2 into nums1 as one sorted array (in-place).

--------------------------------------------------

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]

--------------------------------------------------

Approach (Your Method - Fill + Sort):

1. Fill nums2 elements into nums1 starting from index m
2. Sort nums1 to get the final merged sorted array

--------------------------------------------------

Dry Run:

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

Step 1: Fill nums2 into nums1
→ nums1 = [1,2,3,2,5,6]

Step 2: Sort nums1
→ nums1 = [1,2,2,3,5,6]

--------------------------------------------------

Time Complexity:
O((m+n) log(m+n)) → due to sorting

Space Complexity:
O(1) → in-place modification

--------------------------------------------------

Key Learnings:
- Understand difference between actual values and placeholder zeros
- In-place modification is important
- This approach is simple but not optimal
- Optimal solution uses 3 pointers (O(m+n))

--------------------------------------------------
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # k → pointer for nums2
        k = 0

        # Fill nums2 elements into nums1 after index m
        for l in range(len(nums1)):
            if l >= m:
                nums1[l] = nums2[k]
                k += 1

        # Sort the merged array
        nums1.sort()


# ------------------------------
# Example Run (for testing)
# ------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print("Merged Array:", nums1)