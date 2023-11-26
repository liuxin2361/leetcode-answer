# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur: Optional[ListNode] = head
        pre: Optional[ListNode] = None

        while cur:
            temp: Optional[ListNode] = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return cur
