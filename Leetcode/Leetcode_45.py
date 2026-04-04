from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        LeetCode 45 - Jump Game II

        Goal:
        Find the minimum number of jumps required to reach the last index.

        Approach:
        Greedy (Range-based traversal)
        """

        count = 0   # Number of jumps taken
        m = 0       # Farthest index we can reach so far
        curr = 0    # End of current jump range

        # Traverse till second last index (no need to jump from last index)
        for i in range(len(nums) - 1):

            # Update the farthest reachable index
            # i + nums[i] = maximum distance we can reach from current index
            m = max(m, nums[i] + i)

            # If we reach the end of current range
            if i == curr:
                count += 1        # Take a jump
                curr = m          # Update range to farthest reachable

        return count