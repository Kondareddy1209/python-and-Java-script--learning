class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # No positive product can be less than 1
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        # Expand the sliding window
        for right in range(len(nums)):
            product *= nums[right]

            # Shrink the window while product is invalid
            while product >= k:
                product //= nums[left]
                left += 1

            # Add all valid subarrays ending at 'right'
            count += right - left + 1

        return count