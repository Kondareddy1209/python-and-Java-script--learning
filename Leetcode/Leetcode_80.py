from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array such that each element appears at most twice.
        Modifies the array in-place and returns the new length.

        Example:
        Input:  [1,1,1,2,2,3]
        Output: 5
        Modified array: [1,1,2,2,3,_]
        """

        # Pointer 'i' is the position where we place the next valid element
        i = 1

        # Pointer 'j' is used to iterate through the array
        j = 1

        # 'count' keeps track of occurrences of current element
        count = 1

        # Traverse the array
        while j < len(nums):

            # If current element is same as previous, increment count
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                # If new element found, reset count
                count = 1

            # Allow element only if it appears at most twice
            if count <= 2:
                nums[i] = nums[j]  # Place element at valid position
                i += 1             # Move pointer forward

            # Move to next element
            j += 1

        # 'i' is the new length of the array
        return i