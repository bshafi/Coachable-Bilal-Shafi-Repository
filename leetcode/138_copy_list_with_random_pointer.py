"138. Copy List with Random Pointer"
from typing import Optional

class Node:
    "138. Copy List with Random Pointer"
    def __init__(self, x: int, next = None, random = None): # pylint: disable=W0622
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    "138. Copy List with Random Pointer"
    copies = { None: None }

    a = head
    while a is not None:
        copies[a] = Node(a.val)
        a = a.next

    a = head
    while a is not None:
        copies[a].next = copies[a.next]
        copies[a].random = copies[a.random]
        a = a.next

    return copies[head]
