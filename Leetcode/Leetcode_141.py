"""
LeetCode 141. Linked List Cycle

Problem:
Given the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node in the list can be reached again by continuously
following the next pointers.

Approach: Floyd's Cycle Detection Algorithm (Tortoise and Hare)

1. Initialize two pointers:
   - slow -> moves one step at a time
   - fast -> moves two steps at a time

2. Traverse the list:
   - Move slow by one node.
   - Move fast by two nodes.

3. If there is a cycle:
   - fast will eventually catch up to slow.
   - slow == fast, so return True.

4. If there is no cycle:
   - fast or fast.next becomes None.
   - Return False.

Why it works:
- Inside a cycle, the fast pointer gains one node on the slow pointer
  during each iteration.
- Eventually, the fast pointer will meet the slow pointer.

Time Complexity: O(n)
- Each pointer traverses at most O(n) nodes.

Space Complexity: O(1)
- No extra data structures are used.

Example:
Input:
3 -> 2 -> 0 -> -4
     ^         |
     |_________|

Output:
True
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers at the head
        slow = head
        fast = head

        # Continue while fast can move two steps
        while fast and fast.next:

            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # Reached the end of the list, so no cycle exists
        return False