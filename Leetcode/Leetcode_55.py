class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 'reach' stores the farthest index we can reach so far
        reach = 0
        
        # Traverse through each index
        for i in range(len(nums)):
            
            # If current index is greater than reachable index,
            # it means we cannot reach this position → stuck → return False
            if i > reach:
                return False
            
            # Update the farthest reachable index
            # i + nums[i] = maximum jump from current position
            reach = max(reach, i + nums[i])
            
            # If we can already reach or cross the last index,
            # no need to continue → return True early
            if reach >= len(nums) - 1:
                return True
        
        # If loop completes, we can reach the end
        return True