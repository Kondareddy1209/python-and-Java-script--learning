class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0                    # Left pointer of the sliding window
        s = 0                    # Current window sum
        m = float('inf')         # Stores the minimum valid window length found

        for r in range(len(nums)):   # Expand the window using the right pointer
            s += nums[r]

            # Shrink the window while its sum is at least the target
            while s >= target:
                m = min(m, r - l + 1)  # Update minimum length
                s -= nums[l]           # Remove leftmost element from sum
                l += 1                 # Move left pointer forward

        # Return 0 if no valid subarray exists, otherwise return minimum length
        if m == float('inf') :
            return 0
        else:
            return m