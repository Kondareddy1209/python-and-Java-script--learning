"""
LeetCode 2095 - Delete the Middle Node of a Linked List

Problem:
Given the head of a singly linked list, delete the middle node and return
the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node
(using 0-based indexing).

--------------------------------------------------------------------
APPROACH 1: Two-Pass (Count Nodes)
--------------------------------------------------------------------

Algorithm:
1. Traverse the linked list and count the total number of nodes.
2. Compute the middle position:
      middle = count // 2
3. Traverse again until reaching the middle node.
4. Keep track of the previous node.
5. Delete the middle node:
      prev.next = curr.next

Time Complexity: O(n)
- First traversal: O(n)
- Second traversal: O(n/2)
- Overall: O(n)

Space Complexity: O(1)

--------------------------------------------------------------------
APPROACH 2: Fast & Slow Pointer (Optimal)
--------------------------------------------------------------------

Algorithm:
1. Use two pointers:
      slow -> moves 1 step
      fast -> moves 2 steps
2. Maintain a prev pointer before slow.
3. When fast reaches the end:
      slow points to the middle node.
4. Delete the middle node:
      prev.next = slow.next

Time Complexity: O(n)
- Single traversal.

Space Complexity: O(1)

--------------------------------------------------------------------
Example:
Input:
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Output:
1 -> 3 -> 4 -> 1 -> 2 -> 6
--------------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # --------------------------------------------------------------
    # Approach 1: Two-Pass Counting Method
    # --------------------------------------------------------------
    def deleteMiddle_Counting(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Single node list
        if not head or not head.next:
            return None

        # Count total nodes
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        middle = count // 2

        curr = head
        prev = None
        pos = 0

        # Reach middle node
        while pos < middle:
            prev = curr
            curr = curr.next
            pos += 1

        # Delete middle node
        prev.next = curr.next

        return head

    # --------------------------------------------------------------
    # Approach 2: Fast & Slow Pointer (Optimal)
    # --------------------------------------------------------------
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Single node list
        if not head or not head.next:
            return None

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head


"""
==========================
DRY RUN (Optimal Approach)
==========================

Input:
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Initial:
prev = None
slow = 1
fast = 1

Iteration 1:
prev = 1
slow = 3
fast = 4

Iteration 2:
prev = 3
slow = 4
fast = 1

Iteration 3:
prev = 4
slow = 7
fast = 6

Loop Ends

Middle Node = 7

Delete:
prev.next = slow.next

4 -> 1

Final List:
1 -> 3 -> 4 -> 1 -> 2 -> 6

==========================
COMPLEXITY COMPARISON
==========================

Approach              Time      Space
--------------------------------------
Counting Method       O(n)      O(1)
Fast & Slow Pointer   O(n)      O(1)

Recommended:
✔ Fast & Slow Pointer
Reason:
- Single traversal
- Interview-preferred approach
- Cleaner implementation
"""