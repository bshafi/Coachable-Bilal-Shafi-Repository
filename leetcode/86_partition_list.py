# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''


'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt_head = None
        lt_tail = None

        ge_head = None
        ge_tail = None

        iter = head
        while iter is not None:
            next_node = iter.next

            if iter.val < x:
                if lt_head is None:
                    lt_head = iter
                    lt_tail = iter
                else:
                    lt_tail.next = iter
                    lt_tail = lt_tail.next
            else:
                if ge_head is None:
                    ge_head = iter
                    ge_tail = iter
                else:
                    ge_tail.next = iter
                    ge_tail = ge_tail.next

            iter = next_node

        if lt_tail is not None:
            lt_tail.next = None
        
        if ge_tail is not None:
            ge_tail.next = None

        if lt_tail is not None:
            lt_tail.next = ge_head

            return lt_head
        else:
            return ge_head
        
