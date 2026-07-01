"""
Delete a Node at a Given Position in a Singly Linked List

Problem:
Given the head of a singly linked list and a position `x` (1-based indexing),
delete the node present at that position and return the updated head.

Example:
Input:
    10 -> 20 -> 30 -> 40
    x = 3

Output:
    10 -> 20 -> 40

Approach:
1. Handle the empty linked list.
2. If x == 1, delete the head node by returning head.next.
3. Traverse the linked list until reaching the x-th node.
4. Keep track of:
   - `temp` : current node
   - `prev` : node before the current node
5. Change the previous node's next pointer to skip the node being deleted.

Visualization:

Before deletion (x = 3)

head
 │
 ▼
10 ───► 20 ───► 30 ───► 40 ───► None
         ▲        ▲
       prev     temp

After:
prev.next = temp.next

head
 │
 ▼
10 ───► 20 ─────────► 40 ───► None
           (30 is disconnected)

How the loop works:

Initial:
index = 1
temp = 10
prev = None

Iteration 1:
-----------
prev = 10
temp = 20
index = 2

Iteration 2:
-----------
prev = 20
temp = 30
index = 3

Loop stops because index == x.

Deletion:
---------
prev.next = temp.next

20.next = 40

Result:
10 -> 20 -> 40

Time Complexity:
----------------
O(n)
- In the worst case, we traverse the linked list once.

Space Complexity:
-----------------
O(1)
- Only a few pointer variables are used.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def deleteNode(self, head, x):
        # Empty linked list
        if head is None:
            return None

        # Delete the first node
        if x == 1:
            return head.next

        index = 1
        prev = None
        temp = head

        # Traverse until the x-th node
        while temp and index < x:
            prev = temp
            temp = temp.next
            index += 1

        # If x is greater than the number of nodes
        if temp is None:
            return head

        # Delete the node by skipping it
        prev.next = temp.next

        return head