"""
=========================================================
142. Linked List Cycle II
=========================================================

Problem:
Given the head of a linked list, return the node where the cycle
begins. If there is no cycle, return None.

A cycle exists in a linked list if some node can be reached again
by continuously following the next pointer.

---------------------------------------------------------
Example 1

Input:
head = [3,2,0,-4], pos = 1

Visual:
3 -> 2 -> 0 -> -4
     ^         |
     |_________|

Output:
Node with value 2

Explanation:
The tail connects to the node at index 1, so the cycle starts
at node 2.

---------------------------------------------------------
Example 2

Input:
head = [1,2], pos = 0

Visual:
1 -> 2
^    |
|____|

Output:
Node with value 1

---------------------------------------------------------
Example 3

Input:
head = [1], pos = -1

Output:
None

---------------------------------------------------------
Approach 1: Hash Set
---------------------------------------------------------

Idea:
Store every visited node in a hash set.

Steps:
1. Traverse the linked list.
2. If the current node is already present in the set,
   return that node.
3. Otherwise, add it to the set.
4. If we reach None, no cycle exists.

Why it works:
- The first node visited twice is the starting node
  of the cycle.

Time Complexity:
O(n)

Space Complexity:
O(n)

---------------------------------------------------------
Approach 2: Floyd's Cycle Detection (Tortoise & Hare)
---------------------------------------------------------

Phase 1: Detect Cycle

- Use two pointers:
    slow -> moves 1 step
    fast -> moves 2 steps

- If there is a cycle, they will eventually meet.
- If fast reaches None, no cycle exists.

Phase 2: Find Cycle Start

- Reset slow to head.
- Keep fast at the meeting point.
- Move both one step at a time.
- The node where they meet is the start of the cycle.

Why does this work?

Let:
x = distance from head to cycle start
y = distance from cycle start to meeting point
c = length of cycle

When slow and fast meet:

2(x + y) = x + y + k*c

=> x + y = k*c

=> x = k*c - y

This means the distance from the head to the cycle start
is equal to the distance from the meeting point to the
cycle start.

Therefore, moving both pointers one step at a time makes
them meet exactly at the cycle's starting node.

Time Complexity:
O(n)

Space Complexity:
O(1)

---------------------------------------------------------
Python Solution - Hash Set
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
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return None


"""
---------------------------------------------------------
Python Solution - Floyd's Cycle Detection
---------------------------------------------------------
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Phase 1: Detect Cycle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Phase 2: Find Start of Cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


"""
=========================================================
Comparison
=========================================================

Hash Set:
- Time Complexity: O(n)
- Space Complexity: O(n)
- Easy to understand and implement.

Floyd's Cycle Detection:
- Time Complexity: O(n)
- Space Complexity: O(1)
- Optimal solution and expected in interviews.
"""