"133. Clone Graph"

from typing import Optional

class Node:
    "Graph Node"
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs_copy_nodes(node, copies):
    "Clone Graph"
    if node in copies:
        return copies[node]

    if node is None:
        return None

    new_node = Node(node.val)
    copies[node] = new_node

    new_node.neighbors = [
        dfs_copy_nodes(neighbor_node, copies) for neighbor_node in node.neighbors
    ]


    return new_node

def clone_graph(node: Optional['Node']) -> Optional['Node']:
    "Clone Graph"
    # Copy each node and store them in a hashmap that points from original to new

    # recreate the graph using dfs
    copies = {}
    return dfs_copy_nodes(node, copies)
