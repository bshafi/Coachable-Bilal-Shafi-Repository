"""
Hashmap
LinkedList

pop_node(node) remove node from linked list in O(1)

push_front(node) 

pop_back(node)
"""

class LLNode:
    """
        Linked List
    """
    def __init__(self, val, next=None, prev=None): # pylint: disable=W0622
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    "LRU Cache"
    def __init__(self, capacity: int):
        self.map = {}
        self.size = 0
        self.capacity = capacity

        self.head = None
        self.tail = None

    def pop_node(self, node):
        " Removes node from linked list"
        node_next = node.next
        node_prev = node.prev

        if self.head == node:
            self.head = node_next

        if self.tail == node:
            self.tail = node_prev

        if node_next:
            node_next.prev = node_prev

        if node_prev:
            node_prev.next = node_next

        node.next = None
        node.prev = None

        self.size -= 1

        return node


    def push_front(self, node):
        "Pushes node to front of linked list"
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def pop_back(self):
        "Pops node from back of linked list"
        return self.pop_node(self.tail)

    def get(self, key: int) -> int:
        "Retrieves value from cache. Returns -1 if not found"
        node = self.map.get(key, None)
        if node is None:
            return -1
        else:
            node = self.pop_node(node)
            self.push_front(node)
            return node.val[1]


    def put(self, key: int, value: int) -> None:
        "Sets a value to the cache."
        node = self.map.get(key, None)
        if node is None:
            new_node = LLNode((key, value))
            self.map[key] = new_node
            self.push_front(new_node)
            if self.size > self.capacity:
                last_node = self.pop_back()
                del self.map[last_node.val[0]]
        else:
            node = self.pop_node(node)
            self.push_front(node)
            node.val = (key, value)
