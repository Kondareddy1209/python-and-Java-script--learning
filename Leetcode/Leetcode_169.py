"""
Problem: Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times.

Approach:
- Use a dictionary (hash map) to count the frequency of each element.
- Return the element with the maximum frequency.

Example:
Input: nums = [1, 2, 1, 1, 3, 2, 1]
Output: 1
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the list.

        Steps:
        1. Create a dictionary to store frequencies.
        2. Traverse the list and update counts.
        3. Find the element with maximum frequency.
        4. Return that element.
        """

        # Step 1: Initialize dictionary
        freq = {}

        # Step 2: Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 3: Find element with highest frequency
        majority = max(freq, key=freq.get)

        # Step 4: Return result
        return majority


# -------------------- Execution Example --------------------
if __name__ == "__main__":
    nums = [1, 2, 1, 1, 3, 2, 1]

    solution = Solution()
    result = solution.majorityElement(nums)

    print("Input:", nums)
    print("Majority Element:", result)


"""
Execution Walkthrough:

nums = [1, 2, 1, 1, 3, 2, 1]

Building frequency dictionary:
1 → {1:1}
2 → {1:1, 2:1}
1 → {1:2, 2:1}
1 → {1:3, 2:1}
3 → {1:3, 2:1, 3:1}
2 → {1:3, 2:2, 3:1}
1 → {1:4, 2:2, 3:1}

max(freq, key=freq.get) → 1

Output:
Majority Element: 1
"""


"""
Time Complexity (T.C.):
- Traversing array: O(n)
- Finding max: O(n)
Overall: O(n)

Space Complexity (S.C.):
- Dictionary storage: O(n)
Overall: O(n)
"""


"""
Notes:
- Easy and intuitive solution using hashing.
- For interviews, also learn Boyer-Moore Voting Algorithm (O(1) space).
"""