"""
=========================================================
142. Linked List Cycle II
=========================================================

Problem:
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

A cycle exists in a linked list if some node can be reached again
by continuously following the next pointer.

You must solve it using O(1) extra space.

---------------------------------------------------------
Example 1:
Input:
head = [3,2,0,-4], pos = 1

Visual Representation:
3 -> 2 -> 0 -> -4
     ^         |
     |_________|

Output:
Node with value 2

Explanation:
The tail connects to the node at index 1,
so the cycle starts at node 2.

---------------------------------------------------------
Example 2:
Input:
head = [1,2], pos = 0

Visual Representation:
1 -> 2
^    |
|____|

Output:
Node with value 1

---------------------------------------------------------
Example 3:
Input:
head = [1], pos = -1

Visual Representation:
1 -> None

Output:
None

---------------------------------------------------------
Approach (Floyd's Cycle Detection / Tortoise and Hare)

Step 1: Detect whether a cycle exists.
- Use two pointers:
    slow -> moves one step at a time
    fast -> moves two steps at a time

- If there is no cycle:
    fast reaches None.

- If there is a cycle:
    slow and fast eventually meet.

Step 2: Find the starting node of the cycle.
- Reset slow to head.
- Keep fast at the meeting point.
- Move both pointers one step at a time.
- The node where they meet again is the
  starting node of the cycle.

Why does this work?
Let:
x = distance from head to cycle start
y = distance from cycle start to meeting point
c = length of cycle

When slow and fast meet:

2(x + y) = x + y + k*c

=> x + y = k*c

=> x = k*c - y

This means the distance from head to cycle start
is equal to the distance from meeting point to
cycle start.

Therefore, moving both pointers one step at a time
makes them meet exactly at the cycle's starting node.

---------------------------------------------------------
Time Complexity:
O(n)

- First phase (cycle detection): O(n)
- Second phase (finding cycle start): O(n)

Overall: O(n)

---------------------------------------------------------
Space Complexity:
O(1)

Only two pointers are used.

---------------------------------------------------------
Python Solution
---------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Phase 1: Detect cycle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Phase 2: Find cycle start
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow