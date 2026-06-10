"""
LeetCode 876 - Middle of the Linked List

Problem:
Given the head of a singly linked list, return the middle node.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

----------------------------------------------------------
Approach 1: Counting Nodes (Two Pass)
----------------------------------------------------------

1. Count the total number of nodes.
2. Find middle index:
      middle = count // 2
3. Traverse again to the middle node.
4. Return that node.

Time Complexity: O(n)
Space Complexity: O(1)

----------------------------------------------------------
Approach 2: Fast & Slow Pointer (Optimal)
----------------------------------------------------------

1. Initialize:
      slow = head
      fast = head

2. Move:
      slow -> 1 step
      fast -> 2 steps

3. When fast reaches the end:
      slow will be at the middle.

4. Return slow.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # --------------------------------------------------
    # Approach 1: Counting Method
    # --------------------------------------------------
    def middleNode_Counting(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        middle = count // 2

        curr = head

        for _ in range(middle):
            curr = curr.next

        return curr

    # --------------------------------------------------
    # Approach 2: Fast & Slow Pointer (Optimal)
    # --------------------------------------------------
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


"""
=================================================
Dry Run
=================================================

Input:
1 -> 2 -> 3 -> 4 -> 5

Initial:
slow = 1
fast = 1

Iteration 1:
slow = 2
fast = 3

Iteration 2:
slow = 3
fast = 5

Loop Ends

Return slow = 3

Output:
3 -> 4 -> 5

=================================================
Even Length Example
=================================================

Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6

Initial:
slow = 1
fast = 1

Iteration 1:
slow = 2
fast = 3

Iteration 2:
slow = 3
fast = 5

Iteration 3:
slow = 4
fast = None

Return slow = 4

Output:
4 -> 5 -> 6

Note:
For even-length lists, the problem asks us to
return the SECOND middle node.

=================================================
Complexity Analysis
=================================================

Approach              Time      Space
--------------------------------------
Counting Method       O(n)      O(1)
Fast & Slow Pointer   O(n)      O(1)

Recommended:
✔ Fast & Slow Pointer

Pattern:
✔ Tortoise and Hare (Fast & Slow Pointer)
"""