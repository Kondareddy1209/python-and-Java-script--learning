"""
Problem: Floor in a Sorted Array

Given a sorted array arr[] and an integer x, find the index (0-based)
of the largest element in arr[] that is less than or equal to x.

This element is called the floor of x.

If such an element does not exist, return -1.

Examples:
Input:
arr = [1, 2, 8, 10, 11, 12, 19]
x = 5

Output:
1

Explanation:
The largest element <= 5 is 2, which is present at index 1.


--------------------------------------------------
Approach: Binary Search
--------------------------------------------------

Since the array is sorted, Binary Search can be used.

Observation:
1. If arr[mid] <= x:
   - arr[mid] can be a possible floor.
   - Store mid in ans.
   - Search on the right side to find a larger value
     that is still <= x.

2. If arr[mid] > x:
   - Current element cannot be the floor.
   - Search on the left side.

The last valid stored index will be the answer.

--------------------------------------------------
Dry Run
--------------------------------------------------

arr = [1, 2, 8, 10, 11, 12, 19]
x = 5

Initial:
l = 0
r = 6
ans = -1

Iteration 1:
mid = 3
arr[mid] = 10

10 > 5
Move left

r = 2

----------------------------------

Iteration 2:
l = 0
r = 2

mid = 1
arr[mid] = 2

2 <= 5

Possible floor found
ans = 1

Search right side

l = 2

----------------------------------

Iteration 3:
l = 2
r = 2

mid = 2
arr[mid] = 8

8 > 5

Move left

r = 1

Loop Ends

Answer = 1

--------------------------------------------------
Time Complexity
--------------------------------------------------

Binary Search halves the search space every iteration.

TC = O(log n)

--------------------------------------------------
Space Complexity
--------------------------------------------------

Only a few variables are used.

SC = O(1)

--------------------------------------------------
"""


class Solution:
    def findFloor(self, arr, x):
        """
        Returns the index of the largest element
        less than or equal to x.

        Parameters:
        arr (List[int]): Sorted array
        x (int): Target value

        Returns:
        int: Index of floor element, or -1 if not found
        """

        l = 0
        r = len(arr) - 1

        ans = -1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] <= x:
                # Possible floor found
                ans = mid

                # Search for a larger valid floor
                l = mid + 1

            else:
                # Current element is too large
                r = mid - 1

        return ans


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

if __name__ == "__main__":

    arr = [1, 2, 8, 10, 11, 12, 19]
    x = 5

    sol = Solution()

    result = sol.findFloor(arr, x)

    print("Floor Index:", result)

    if result != -1:
        print("Floor Value:", arr[result])
    else:
        print("No floor exists.")