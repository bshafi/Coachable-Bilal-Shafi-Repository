"""
    Partition list
"""

from typing import Optional

class ListNode:
    """
        Definition for singly-linked list.
    """
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    """
        Solution to leetcode
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
            Patitions a linked list
        """
        lt_head = None
        lt_tail = None

        ge_head = None
        ge_tail = None

        ptr = head
        while ptr is not None:
            next_node = ptr.next

            if ptr.val < x:
                if lt_head is None:
                    lt_head = ptr
                    lt_tail = ptr
                else:
                    lt_tail.next = ptr
                    lt_tail = lt_tail.next
            else:
                if ge_head is None:
                    ge_head = ptr
                    ge_tail = ptr
                else:
                    ge_tail.next = ptr
                    ge_tail = ge_tail.next

            ptr = next_node

        if lt_tail is not None:
            lt_tail.next = None

        if ge_tail is not None:
            ge_tail.next = None

        if lt_tail is not None:
            lt_tail.next = ge_head

            return lt_head
        return ge_head
