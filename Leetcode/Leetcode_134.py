from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        LeetCode 134 - Gas Station

        Goal:
        Find the starting gas station index from which we can complete the circuit once.
        If not possible, return -1.

        Approach:
        Greedy
        """

        # Step 1: If total gas is less than total cost → impossible
        if sum(gas) < sum(cost):
            return -1

        start = 0   # candidate starting index
        tank = 0    # current gas in tank

        # Step 2: Traverse all stations
        for i in range(len(gas)):

            # Net gas after reaching next station
            diff = gas[i] - cost[i]
            tank += diff

            # If tank becomes negative → cannot start from 'start'
            if tank < 0:
                start = i + 1   # move start to next station
                tank = 0        # reset tank

        # Step 3: Return valid starting index
        return start