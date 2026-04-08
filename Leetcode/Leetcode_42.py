# LeetCode 42: Trapping Rain Water
# Approach: Prefix Max Arrays (Left Max & Right Max)

# Time Complexity (T.C): O(n)
# - We traverse the array 3 times:
#   1. To build l_max
#   2. To build r_max
#   3. To calculate trapped water
#
# Space Complexity (S.C): O(n)
# - We use two extra arrays (l_max and r_max) of size n

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # Edge case: if array is empty, no water can be trapped
        if n == 0:
            return 0
        
        # Arrays to store maximum height from left and right
        l_max = [0] * n
        r_max = [0] * n
        
        water = 0  # Total trapped water
        
        # Step 1: Fill left max array
        # l_max[i] stores the maximum height from index 0 to i
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        
        # Step 2: Fill right max array
        # r_max[i] stores the maximum height from index i to n-1
        r_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])
        
        # Step 3: Calculate trapped water
        # Water at each index = min(left max, right max) - height[i]
        for i in range(n):
            water += min(l_max[i], r_max[i]) - height[i]
        
        return water