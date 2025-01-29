"""
129. Sum Root to Leaf Numbers
"""
from typing import Optional

class TreeNode:
    "TreeNode"
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, cur_num):
    """
        129. Sum Root to Leaf Numbers
    """
    if node is None:
        return 0

    new_num = cur_num * 10 + node.val

    if node.left is None and node.right is None:
        return new_num
    else:
        return dfs(node.left, new_num) + dfs(node.right, new_num)

def sum_numbers(root: Optional[TreeNode]) -> int:
    """
        129. Sum Root to Leaf Numbers
    """
    return dfs(root, 0)
