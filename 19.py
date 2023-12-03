# 19.Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return
        dummy_head: ListNode = ListNode(next=head)
        fast: ListNode = dummy_head
        slow: ListNode = dummy_head
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next
