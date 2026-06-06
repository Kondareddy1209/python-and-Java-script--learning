class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array containing only 0s, 1s, and 2s in-place
        using the Dutch National Flag Algorithm.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        # Pointer for the next position of 0
        low = 0
        
        # Pointer for the next position of 2
        high = len(nums) - 1
        
        # Current element being processed
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                # Place 0 at the beginning section
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in the correct section
                mid += 1

            else:
                # Place 2 at the ending section
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums