# ============================================
# LeetCode 206 - Reverse Linked List
# ============================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # --------------------------------------------------
    # Method 1: Standard Approach (using head pointer)
    # --------------------------------------------------
    def reverseList_standard(self, head):
        """
        Reverse a singly linked list using head pointer.

        Steps:
        1. Traverse the list
        2. Reverse links one by one
        3. Return new head (prev)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        prev = None  # Will become new head

        while head:
            curr = head           # store current node
            head = head.next     # move head forward
            curr.next = prev     # reverse link
            prev = curr          # move prev forward

        return prev


    # --------------------------------------------------
    # Method 2: Using temp pointer (your approach - fixed)
    # --------------------------------------------------
    def reverseList(self, head):
        """
        Reverse a singly linked list using temp pointer.

        Key Idea:
        - Use 'temp' as traversal pointer
        - Loop condition must match traversal pointer

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        prev = None
        temp = head  # traversal pointer

        while temp:
            curr = temp.next   # store next node
            temp.next = prev   # reverse link
            prev = temp        # move prev forward
            temp = curr        # move temp forward

        return prev