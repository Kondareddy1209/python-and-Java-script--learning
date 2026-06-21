"""
Problem: Ceil in a Sorted Array

Given a sorted array nums[] and an integer x,
find the index (0-based) of the smallest element
that is greater than or equal to x.

This element is called the ceil of x.

If such an element does not exist, return -1.

Examples:
Input:
nums = [1, 2, 8, 10, 11, 12, 19]
x = 5

Output:
2

Explanation:
The smallest element >= 5 is 8,
which is present at index 2.

--------------------------------------------------
Approach: Binary Search
--------------------------------------------------

Since the array is sorted, Binary Search can be used.

Observation:

1. If nums[mid] >= x:
   - nums[mid] can be a possible ceil.
   - Store mid in ans.
   - Search on the left side to find a smaller value
     that is still >= x.

2. If nums[mid] < x:
   - Current element cannot be the ceil.
   - Search on the right side.

The last valid stored index will be the answer.

--------------------------------------------------
Dry Run
--------------------------------------------------

nums = [1, 2, 8, 10, 11, 12, 19]
x = 5

Initial:
l = 0
r = 6
ans = -1

Iteration 1:
mid = 3
nums[mid] = 10

10 >= 5

Possible ceil found
ans = 3

Search left side

r = 2

----------------------------------

Iteration 2:
l = 0
r = 2

mid = 1
nums[mid] = 2

2 < 5

Move right

l = 2

----------------------------------

Iteration 3:
l = 2
r = 2

mid = 2
nums[mid] = 8

8 >= 5

Possible ceil found
ans = 2

Search left side

r = 1

Loop Ends

Answer = 2

--------------------------------------------------
Time Complexity
--------------------------------------------------

Binary Search reduces the search space by half
in every iteration.

TC = O(log n)

--------------------------------------------------
Space Complexity
--------------------------------------------------

Only a few variables are used.

SC = O(1)

--------------------------------------------------
"""


class Solution:
    def findCeil(self, nums, x):
        """
        Returns the index of the smallest element
        greater than or equal to x.

        Parameters:
        nums (List[int]): Sorted array
        x (int): Target value

        Returns:
        int: Index of ceil element, or -1 if not found
        """

        ans = -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= x:
                # Possible ceil found
                ans = mid

                # Search for a smaller valid ceil
                r = mid - 1

            else:
                # Current element is too small
                l = mid + 1

        return ans


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

if __name__ == "__main__":

    nums = [1, 2, 8, 10, 11, 12, 19]
    x = 5

    sol = Solution()

    result = sol.findCeil(nums, x)

    print("Ceil Index:", result)

    if result != -1:
        print("Ceil Value:", nums[result])
    else:
        print("No ceil exists.")