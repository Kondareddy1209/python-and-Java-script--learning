"""
LeetCode 1732 - Find the Highest Altitude

This file contains two approaches:

1. Optimized Prefix Sum (O(1) space)  ✅ Recommended
2. Prefix Sum Array (O(n) space)     📘 For learning

---------------------------------------------------
PROBLEM:
You are given an array 'gain' where gain[i] represents 
the net altitude change between points.

You start at altitude = 0.

Return the highest altitude reached.

---------------------------------------------------
EXAMPLE:
Input: gain = [-5, 1, 5, 0, -7]
Output: 1

Explanation:
Altitude sequence:
0 → -5 → -4 → 1 → 1 → -6

Highest altitude = 1
---------------------------------------------------
"""


class Solution:
    def largestAltitude(self, gain):
        """
        APPROACH 1: Optimized Prefix Sum

        IDEA:
        - Instead of storing all altitudes, we calculate on the fly
        - Keep track of:
            curr    -> current altitude
            max_al  -> maximum altitude seen so far

        HOW IT WORKS:
        Example: gain = [-5, 1, 5]

        Step 1: curr = 0 + (-5) = -5
        Step 2: curr = -5 + 1 = -4
        Step 3: curr = -4 + 5 = 1

        Track max during the process.

        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY: O(1)
        """

        curr = 0       # current altitude
        max_al = 0     # highest altitude

        for g in gain:
            curr += g
            max_al = max(max_al, curr)

        return max_al


class SolutionPrefixArray:
    def largestAltitude(self, gain):
        """
        APPROACH 2: Prefix Sum Array

        IDEA:
        - Build an array storing altitude at each step
        - Then return max value from it

        prefix[i] = sum of gain from 0 to i-1

        HOW IT WORKS:
        gain = [-5, 1, 5]

        prefix = [0]
        prefix = [0, -5]
        prefix = [0, -5, -4]
        prefix = [0, -5, -4, 1]

        max(prefix) = 1

        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY: O(n)
        """

        prefix = [0]  # starting altitude

        for g in gain:
            prefix.append(prefix[-1] + g)

        return max(prefix)


# -------------------------------
# DRIVER CODE (for testing)
# -------------------------------
if __name__ == "__main__":
    gain = [-5, 1, 5, 0, -7]

    sol1 = Solution()
    sol2 = SolutionPrefixArray()

    print("Optimized Approach Output:", sol1.largestAltitude(gain))
    print("Prefix Array Approach Output:", sol2.largestAltitude(gain))


"""
---------------------------------------------------
KEY LEARNING:

✔ This is a PREFIX SUM problem
✔ Altitude = Running Sum (prefix sum)
✔ Answer = Maximum Prefix Sum

---------------------------------------------------
WHEN TO USE WHICH?

1. Use Optimized Version:
   - When only max/min is needed
   - Saves memory

2. Use Prefix Array:
   - When all intermediate values are needed
   - Useful in advanced problems

---------------------------------------------------
INTERVIEW TIP:

If asked:
"What pattern is this?"

Answer:
"This is a prefix sum problem where we track the maximum prefix sum."

---------------------------------------------------
"""