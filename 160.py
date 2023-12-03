# 160. Intersection of Two Linked Lists

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_len: int = self.getLength(headA)
        headB_len: int = self.getLength(headB)

        if headA_len - headB_len > 0:
            headA = self.moveForward(headA, headA_len - headB_len)
        else:
            headB = self.moveForward(headB, headB_len - headA_len)

        while headA:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None

    def getLength(self, listNode: ListNode) -> int:
        length: int = 0
        cur = listNode
        while cur:
            length += 1
            cur = cur.next
        return length

    def moveForward(self, head: ListNode, step: int) -> Optional[ListNode]:
        res: ListNode = head
        while step > 0:
            res = res.next
            step -= 1

        return res
