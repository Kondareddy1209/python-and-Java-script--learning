from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        LeetCode 74. Search a 2D Matrix

        Idea:
        Treat the matrix as a single sorted 1D array and perform
        binary search on the virtual array.

        Mapping:
            index -> (row, col)

            row = index // number_of_columns
            col = index % number_of_columns

        Example:
            Matrix:
            [
                [1, 3, 5],
                [7, 9, 11]
            ]

            Virtual array:
            [1, 3, 5, 7, 9, 11]

            Index mapping:
            0 -> (0, 0)
            1 -> (0, 1)
            2 -> (0, 2)
            3 -> (1, 0)
            4 -> (1, 1)
            5 -> (1, 2)

        Time Complexity:
            O(log(m * n))

        Space Complexity:
            O(1)
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # Binary search over the virtual 1D array
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Convert virtual index to matrix coordinates
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False