# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

from typing import Optional, Set


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        list_node_set: Set[ListNode] = set()
        len_set: int = 0
        fast: ListNode = head

        while fast:
            list_node_set.add(fast)
            len_set += 1
            if len_set != len(list_node_set):
                return fast

            fast = fast.next

        return None

# 方法2
# https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E6%80%9D%E8%B7%AF
