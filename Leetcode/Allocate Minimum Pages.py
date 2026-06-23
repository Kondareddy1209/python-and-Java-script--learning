"""
Problem: Allocate Minimum Pages

Given an array arr[] where each element represents the number of pages in a book
and an integer k representing the number of students, allocate books such that:

1. Each student gets at least one book.
2. Each book is assigned to exactly one student.
3. Books must be allocated in contiguous order.
4. Minimize the maximum number of pages assigned to any student.

Approach:
- Use Binary Search on the answer.
- The minimum possible answer is max(arr) because a student must read
  at least the largest book.
- The maximum possible answer is sum(arr) because one student can read all books.
- For a given maximum page limit (mid), check if allocation is possible
  using at most k students.

Time Complexity:
- Feasibility Check: O(n)
- Binary Search Range: O(log(sum(arr) - max(arr)))
- Overall: O(n * log(sum(arr)))

Space Complexity:
- O(1)

Example:
Input:
arr = [12, 34, 67, 90]
k = 2

Output:
113

Explanation:
Student 1 -> [12, 34, 67] = 113 pages
Student 2 -> [90] = 90 pages

Maximum pages assigned = 113
This is the minimum possible maximum allocation.
"""


class Solution:
    def findPages(self, arr, k):
        """
        Finds the minimum possible maximum pages assigned to any student.

        Args:
            arr (List[int]): Pages in each book
            k (int): Number of students

        Returns:
            int: Minimum possible maximum pages allocation
        """

        # More students than books is invalid
        if k > len(arr):
            return -1

        # Search space
        left = max(arr)
        right = sum(arr)

        while left <= right:
            mid = left + (right - left) // 2

            if self.can_allocate(mid, arr, k):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_allocate(self, max_pages, arr, k):
        """
        Checks whether books can be allocated to at most k students
        such that no student gets more than max_pages.

        Args:
            max_pages (int): Candidate answer
            arr (List[int]): Pages in each book
            k (int): Number of students

        Returns:
            bool: True if allocation is possible, otherwise False
        """

        students = 1
        current_pages = 0

        for pages in arr:

            # Continue assigning books to current student
            if current_pages + pages <= max_pages:
                current_pages += pages

            # Assign to next student
            else:
                students += 1
                current_pages = pages

        return students <= k


# --------------------------
# Driver Code
# --------------------------
if __name__ == "__main__":

    arr = [12, 34, 67, 90]
    k = 2

    solution = Solution()
    answer = solution.findPages(arr, k)

    print("Books:", arr)
    print("Students:", k)
    print("Minimum Maximum Pages:", answer)

"""
Dry Run:

arr = [12, 34, 67, 90]
k = 2

Search Space:
left = 90
right = 203

mid = 146
Allocation possible with 2 students
Move left -> search smaller answer

mid = 117
Allocation possible
Move left

mid = 103
Requires 3 students
Move right

mid = 110
Requires 3 students
Move right

mid = 113
Possible with 2 students

Final Answer = 113

--------------------------------

Binary Search Pattern:

Minimum Valid Answer:

while left <= right:
    mid = left + (right - left) // 2

    if valid(mid):
        right = mid - 1
    else:
        left = mid + 1

return left

--------------------------------

Key Insight:

We are NOT searching inside the array.

We are searching on the answer space:

[max(arr), sum(arr)]

This is a classic "Binary Search on Answer" problem.
"""