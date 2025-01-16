"""
    Range sum of bst
"""


from typing import Optional

class TreeNode:
    """
        Definition of TreeNode
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_of_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
    """
        Range sum of BST
    """
    if root is None:
        return 0
    total = 0
    if root.val < high:
        total += self.rangeSumBST(root.right, low, high)
    if root.val > low:
        total += self.rangeSumBST(root.left, low, high)
    if low <= root.val <= high:
        total += root.val
    return total
