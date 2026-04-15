"""
File: delete_duplicates_linkedlist.py

Problem:
---------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

This problem is commonly asked in coding interviews and platforms like LeetCode.

Approach:
---------
We traverse the linked list using a pointer (temp).
Since the list is sorted, duplicate elements will always be adjacent.

Steps:
1. Start from the head node.
2. Compare current node with next node.
3. If values are same → skip the next node.
4. Else → move forward.
5. Continue until end of list.

"""

from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Function to remove duplicates from a sorted linked list.

        Parameters:
        -----------
        head : ListNode
            Head of the linked list

        Returns:
        --------
        ListNode
            Head of the modified linked list (without duplicates)
        """

        temp = head

        # Traverse the list until last node
        while temp != None and temp.next != None:

            # If duplicate found
            if temp.val == temp.next.val:
                # Skip the next node
                temp.next = temp.next.next
            else:
                # Move forward
                temp = temp.next

        return head


# -------------------------------
# 🔍 Example Usage
# -------------------------------
if __name__ == "__main__":
    """
    Example:
    Input:  1 -> 1 -> 2 -> 3 -> 3
    Output: 1 -> 2 -> 3
    """

    # Creating linked list manually
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    # Apply solution
    sol = Solution()
    result = sol.deleteDuplicates(head)

    # Print result
    print("Linked List after removing duplicates:")
    temp = result
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


# -------------------------------
# ⏱ Complexity Analysis
# -------------------------------

"""
Time Complexity:
---------------
O(n)
- We traverse the linked list once.

Space Complexity:
----------------
O(1)
- No extra space is used (in-place modification).

"""

# -------------------------------
# 🧠 Workflow Explanation
# -------------------------------

"""
Example Walkthrough:

Input:
1 -> 1 -> 2 -> 3 -> 3

Step 1:
temp = 1, next = 1 → duplicate → remove one

List becomes:
1 -> 2 -> 3 -> 3

Step 2:
temp = 1, next = 2 → not equal → move forward

Step 3:
temp = 2, next = 3 → not equal → move forward

Step 4:
temp = 3, next = 3 → duplicate → remove one

Final Output:
1 -> 2 -> 3

"""

# -------------------------------
# 🚀 Key Learning Points
# -------------------------------

"""
✔ Always check:
    temp != None and temp.next != None

✔ Why?
    To avoid accessing None.next (which causes error)

✔ Important:
    Move pointer forward ONLY when no deletion happens

✔ Since list is sorted:
    Duplicates are always adjacent → easy removal

"""