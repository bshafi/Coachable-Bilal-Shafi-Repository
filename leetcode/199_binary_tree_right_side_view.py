"199. Binary Tree Right Side View"

from typing import Optional, List

class TreeNode:
    "199. Binary Tree Right Side View"
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side(node, height, arr):
    "199. Binary Tree Right Side View"
    if node is None:
        return

    if height >= len(arr):
        arr.append(node.val)
    else:
        arr[height] = node.val

    right_side(node.left, height + 1, arr)
    right_side(node.right, height + 1, arr)

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    "199. Binary Tree Right Side View"
    arr = []
    right_side(root, 0, arr)
    return arr
