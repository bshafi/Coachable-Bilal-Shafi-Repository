"863. All Nodes Distance K in Binary Tree"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

def find_parents(node, prev, parents):
    "Finds parents"
    if node is None:
        return

    parents[node] = prev

    find_parents(node.left, node, parents)
    find_parents(node.right, node, parents)

def dfs(node, dist, k, parents, visited, nodes):
    "863. All Nodes Distance K in Binary Tree"
    if node is None or node in visited:
        return

    visited.add(node)

    if dist == k:
        nodes.append(node.val)
    else:
        dfs(parents[node], dist + 1, k, parents, visited, nodes)
        dfs(node.left, dist + 1, k, parents, visited, nodes)
        dfs(node.right, dist + 1, k, parents, visited, nodes)

def distance_k(root, target, k: int) -> List[int]:
    "863. All Nodes Distance K in Binary Tree"
    nodes = []
    visited = set()
    parents = {}

    find_parents(root, None, parents)


    dfs(target, 0, k, parents, visited, nodes)

    return nodes
