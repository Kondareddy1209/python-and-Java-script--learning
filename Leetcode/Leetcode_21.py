"""
LeetCode 21. Merge Two Sorted Lists

Problem:
You are given the heads of two sorted linked lists, list1 and list2.

Merge the two lists into one sorted linked list and return the head
of the merged list.

Example:
Input:
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4

---------------------------------------------------------
Approach: Recursive
---------------------------------------------------------

Idea:
Since both linked lists are already sorted, compare the current
nodes of both lists.

1. If list1's value is smaller (or equal), choose list1's node.
2. Recursively merge the remaining nodes of list1 with list2.
3. If list2's value is smaller, choose list2's node.
4. Recursively merge list1 with the remaining nodes of list2.
5. Continue until one list becomes empty.

Base Cases:
- If list1 is empty, return list2.
- If list2 is empty, return list1.

Why it works:
At every recursive call, the smallest available node is placed
into the merged list, maintaining sorted order.

---------------------------------------------------------
Dry Run
---------------------------------------------------------

list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4

Compare:
1 <= 1

Choose first 1

1 -> merge(2->4, 1->3->4)

Compare:
2 > 1

Choose second 1

1 -> merge(2->4, 3->4)

Compare:
2 <= 3

Choose 2

2 -> merge(4, 3->4)

Compare:
4 > 3

Choose 3

3 -> merge(4, 4)

Compare:
4 <= 4

Choose first 4

4 -> merge(None, 4)

Return remaining list:

4

Final Result:

1 -> 1 -> 2 -> 3 -> 4 -> 4

---------------------------------------------------------
Time Complexity: O(m + n)
---------------------------------------------------------
m = length of list1
n = length of list2

Each node is visited exactly once.

---------------------------------------------------------
Space Complexity: O(m + n)
---------------------------------------------------------
Recursive call stack can grow up to m + n calls.

---------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Base Case 1:
        # If list1 is empty, return list2
        if list1 is None:
            return list2

        # Base Case 2:
        # If list2 is empty, return list1
        if list2 is None:
            return list1

        # Choose the smaller node
        if list1.val <= list2.val:

            # Merge the remaining nodes
            list1.next = self.mergeTwoLists(
                list1.next,
                list2
            )

            return list1

        else:

            # Merge the remaining nodes
            list2.next = self.mergeTwoLists(
                list1,
                list2.next
            )

            return list2