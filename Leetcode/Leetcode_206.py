# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Approach:
        - Use three pointers: prev, curr (head), and next (implicit)
        - Iterate through the list and reverse the direction of each node

        Time Complexity: O(n)  -> Traverse the list once
        Space Complexity: O(1) -> In-place reversal, no extra memory used
        """

        # 'prev' will become the new head of reversed list
        prev = None

        # Traverse until head becomes None
        while head:
            # Step 1: Store current node
            curr = head

            # Step 2: Move head to next node
            # (important to not lose the rest of the list)
            head = head.next

            # Step 3: Reverse the link
            curr.next = prev

            # Step 4: Move prev forward
            prev = curr

        # At the end, prev will be the new head
        return prev