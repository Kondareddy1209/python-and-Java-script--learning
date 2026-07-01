# ============================================================
# 160. Intersection of Two Linked Lists
# ============================================================
# Given the heads of two singly linked lists, return the node
# at which the two lists intersect. If the two linked lists
# have no intersection, return None.
#
# ------------------------------------------------------------
# Approach 1: Length Difference (Optimal)
# ------------------------------------------------------------
# Idea:
# 1. Find the lengths of both linked lists.
# 2. Move the pointer of the longer list ahead by the
#    difference in lengths.
# 3. Move both pointers together until they meet.
#
# Time Complexity : O(m + n)
# Space Complexity: O(1)
#
# ------------------------------------------------------------
# Approach 2: Two Pointer Switching (Most Optimal)
# ------------------------------------------------------------
# Idea:
# 1. Start one pointer at headA and another at headB.
# 2. When a pointer reaches the end, redirect it to the
#    other list's head.
# 3. They will either meet at the intersection node or
#    both become None.
#
# Time Complexity : O(m + n)
# Space Complexity: O(1)
#
# ------------------------------------------------------------
# Approach 3: Hash Set
# ------------------------------------------------------------
# Idea:
# 1. Store every node of the first linked list in a hash set.
# 2. Traverse the second list.
# 3. The first node already present in the set is the
#    intersection node.
#
# Time Complexity : O(m + n)
# Space Complexity: O(m)
# ============================================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # =====================================================
        # Approach 1 : Length Difference
        # =====================================================
        """
        def length(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        l1 = length(headA)
        l2 = length(headB)

        while l1 > l2:
            headA = headA.next
            l1 -= 1

        while l2 > l1:
            headB = headB.next
            l2 -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
        """

        # =====================================================
        # Approach 2 : Two Pointer Switching
        # =====================================================
        """
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
        """

        # =====================================================
        # Approach 3 : Hash Set
        # =====================================================
        visited = set()

        current = headA
        while current:
            visited.add(current)
            current = current.next

        current = headB
        while current:
            if current in visited:
                return current
            current = current.next

        return None